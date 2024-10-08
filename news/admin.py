from django.contrib import admin
from .models import Thread, Response
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Thread)
class ThreadAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

# Register your models here.
admin.site.register(Response)
