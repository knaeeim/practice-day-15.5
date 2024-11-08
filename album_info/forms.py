from .models import Album
from django import forms

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__" # This will include all fields in the form
        
    release_date = forms.DateField(
        widget=forms.DateInput(attrs = {'type': 'date'})
    )