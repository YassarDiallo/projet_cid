from django import forms 
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=["extrait","certificat","photos","reçu"]
        