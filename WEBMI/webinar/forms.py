from django import forms
from .models import Inscription  # Ton modèle d’inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'  # Ou spécifie les champs si nécessaire