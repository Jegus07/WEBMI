from django.urls import path
from . import views
from .views import inscription,InscritView


urlpatterns = [
    path('', views.inscription, name='inscription'),  # ← rendre accessible via /inscription/
    path('', inscription, name='inscription'),
    path('dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('export/excel/', views.exporter_inscrits_excel, name='exporter_inscrits_excel'),
    path('export/pdf/', views.exporter_inscrits_pdf, name='exporter_inscrits_pdf'),
    path('dashboard/', InscritView.as_view(), name='dashboard'),
]

