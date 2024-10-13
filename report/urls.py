from . import views
from django.urls import path

urlpatterns = [
    path('', views.report_guide, name='report'),
]