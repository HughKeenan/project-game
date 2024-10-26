from .models import Response, Thread
from django import forms

# form to post and edit responses
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('content',)

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'body',)        
   