from . import views
from django.urls import path

urlpatterns = [
    path('', views.report_user, name='report'),
]