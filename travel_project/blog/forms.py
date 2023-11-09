from django import forms
from .models import Post, Destino, Comunidad

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'

class ComunidadForm(forms.ModelForm):
    class Meta:
        model = Comunidad
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)