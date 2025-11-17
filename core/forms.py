from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nom', 'prenom', 'email', 'telephone', 'sujet', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre nom',
                'required': True
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre prénom',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'votre.email@example.com',
                'required': True
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+224 XX XXX XX XX (optionnel)'
            }),
            'sujet': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sujet de votre message',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Votre message...',
                'rows': 6,
                'required': True
            }),
        }
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'email': 'Email',
            'telephone': 'Téléphone',
            'sujet': 'Sujet',
            'message': 'Message',
        }

