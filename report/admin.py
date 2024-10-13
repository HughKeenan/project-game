from django.contrib import admin
from .models import Report
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Report)
class ReportAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)