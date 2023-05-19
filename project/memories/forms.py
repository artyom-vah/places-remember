from django import forms

from .models import Place


class AddPlaceForm(forms.ModelForm):    
    class Meta:
        model = Place
        fields = ('title', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})       
        }