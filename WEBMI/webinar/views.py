from django.shortcuts import render
from .forms import InscriptionForm  # Assure-toi d'avoir ce formulaire

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'webinar/success.html')
    else:
        form = InscriptionForm()
    return render(request, 'webinar/inscription.html', {'form': form})
