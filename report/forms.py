from .models import ReportUser
from django import forms


class ReportUserForm(forms.ModelForm):
    class Meta:
        model = ReportUser
        fields = ('thread_url','user_being_reported','reason_for_report','reporters_email',)