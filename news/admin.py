from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Thread, Response


@admin.register(Thread)
class ThreadAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', "posted_on")
    search_fields = ['title', 'posted_on']
    list_filter = ('posted_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


@admin.register(Response)
class ResponseAdmin(SummernoteModelAdmin):
    list_display = ('thread', 'poster', "posted_on")
    search_fields = ['thread', 'poster', 'posted_on']
    list_filter = ('posted_on', 'poster',)
    summernote_fields = ('content',)
