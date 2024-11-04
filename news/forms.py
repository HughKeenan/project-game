from django import forms
from .models import Response, Thread


# form to post and edit responses
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('content',)
