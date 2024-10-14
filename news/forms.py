from .models import Response
from django import forms


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('body',)