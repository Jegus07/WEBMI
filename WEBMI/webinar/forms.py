from django import forms
from .models import Inscription,Inscrit # Ton modèle d’inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscrit
        fields = ['nom', 'email', 'telephone', 'profession']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'}),
        }
