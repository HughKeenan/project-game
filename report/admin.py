"""admin for the report app"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Report, ReportUser


@admin.register(Report)
class ReportAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


@admin.register(ReportUser)
class ReportUserAdmin(SummernoteModelAdmin):

    list_display = ('reason_for_report', 'examined',)
