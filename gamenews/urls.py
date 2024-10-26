"""
url configuration for gamenews project
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("report/", include("report.urls"), name="report-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path("", include("news.urls"), name="news-urls"),
    path('summernote/', include('django_summernote.urls')),
]
