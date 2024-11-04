"""forms for the news app"""
from django import forms
from .models import Response, Thread


# form to respond to posts
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('content',)
