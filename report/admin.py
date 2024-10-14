from django.contrib import admin
from .models import Report, ReportUser
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Report)
class ReportAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(ReportUser)
class ReportUserAdmin(SummernoteModelAdmin):

    list_display = ('reason_for_report', 'examined',)    