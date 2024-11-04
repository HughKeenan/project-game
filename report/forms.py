"""forms for the report app"""
from django import forms
from .models import ReportUser


# form to report users
class ReportUserForm(forms.ModelForm):
    class Meta:
        model = ReportUser
        fields = ('thread_url', 'user_being_reported',
                  'reason_for_report', 'reporters_email',)
