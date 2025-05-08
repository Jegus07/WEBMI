from django.shortcuts import render
from django.views import View
from .forms import InscriptionForm  # Assure-toi d'avoir ce formulaire
from django.contrib.admin.views.decorators import staff_member_required
import openpyxl
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.db.models import Q
from .models import Inscrit



def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'webinar/success.html')
    else:
        form = InscriptionForm()
        #exemple un nouveau
    return render(request, 'webinar/inscription.html', {'form': form})

@staff_member_required
def dashboard_admin(request):
    inscrits = Inscrit.objects.all().order_by('-date_inscription')
    total = inscrits.count()
    return render(request, 'webinar/dashboard.html', {'inscrits': inscrits, 'total': total})

@staff_member_required
def exporter_inscrits_excel(request):
    inscrits = Inscrit.objects.all()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inscrits Webinaire"

    # En-têtes
    headers = ["Nom", "Email", "Téléphone", "Profession", "Date d'inscription"]
    ws.append(headers)

    # Contenu
    for inscrit in inscrits:
        ws.append([
            inscrit.nom,
            inscrit.email,
            inscrit.telephone,
            inscrit.profession,
            inscrit.date_inscription.strftime("%d/%m/%Y %H:%M")
        ])

    # Réponse HTTP avec fichier Excel
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = "attachment; filename=inscrits_webinaire.xlsx"
    wb.save(response)
    return response

@staff_member_required
def exporter_inscrits_pdf(request):
    inscrits = InscriptionForm.objects.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="inscrits_webinaire.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    y = height - 50
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, y, "Liste des inscrits au webinaire")
    y -= 30

    p.setFont("Helvetica", 10)
    headers = ["Nom", "Email", "Téléphone", "Profession", "Date"]
    p.drawString(50, y, " | ".join(headers))
    y -= 20

    for inscrit in inscrits:
        line = f"{inscrit.nom} | {inscrit.email} | {inscrit.telephone} | {inscrit.profession} | {inscrit.date_inscription.strftime('%d/%m/%Y')}"
        if y < 50:
            p.showPage()
            y = height - 50
        p.drawString(50, y, line)
        y -= 20

    p.showPage()
    p.save()
    return response


def dashboard(request):
    query = request.GET.get("q")
    if query:
        inscrits = Inscrit.objects.filter(
            Q(nom__icontains=query) |
            Q(email__icontains=query) |
            Q(telephone__icontains=query) |
            Q(profession__icontains=query)
        )
    else:
        inscrits = Inscrit.objects.all()

    return render(request, 'webinar/dashboard.html', {'inscrits': inscrits})

class InscritView(View):
    template_name = 'webinar/dashboard.html'

    def get(self, request):
        query = request.GET.get("q", "")
        if query:
            inscrits = Inscrit.objects.filter(
                Q(nom__icontains=query) |
                Q(email__icontains=query) |
                Q(telephone__icontains=query) |
                Q(profession__icontains=query)
            )
        else:
            inscrits = Inscrit.objects.all()

        context = {
            'inscrits': inscrits,
            'query': query
        }
        return render(request, self.template_name, context)