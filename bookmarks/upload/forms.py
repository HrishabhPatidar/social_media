from django import forms

from .models import ImageUpload

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ('caption', 'image')
        widget = {'username': forms.HiddenInput}





