from . import views
from django.urls import path

urlpatterns = [
    path('', views.ThreadList.as_view(), name='threadlist'),
]