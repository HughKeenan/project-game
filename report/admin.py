from django.contrib import admin
from .models import Report
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Report)
class ReportAdmin(SummernoteModelAdmin):
    list_display = ('reported_user', 'reason_for_report')
    search_fields = ['thread_url', 'reported_user', 'reason_for_report']
    list_filter = ('reported_user',)
    summernote_fields = ('reason_for_report',)