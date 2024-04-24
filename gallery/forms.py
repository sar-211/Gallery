from django import forms
from .models import Images

class ImageForms(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['title', 'description', 'image', 'location']