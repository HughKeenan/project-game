from . import views
from django.urls import path

# url patterns for report app
urlpatterns = [
    path('', views.report_guide, name='report'),
]
