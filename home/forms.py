from django import forms
from .models import Genre


class GenreCreateForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    created = forms.DateTimeField()    


class GenreUpdateForm(forms.ModelForm):
    class Meta :
        model = Genre
        fields = ('name', 'description', 'created')
