"""urls for report app"""
from django.urls import path
from . import views


# url patterns for report app
urlpatterns = [
    path('', views.report_guide, name='report'),
]
