from . import views
from django.urls import path

"""
url patterns for news app
"""

urlpatterns = [
    path('', views.ThreadList.as_view(), name='threadlist'),
    path('<slug:slug>/', views.thread_detail, name='thread_detail'),
    path('welcome-to-the-site/', views.thread_detail, name='about_us'),
    path('<slug:slug>/edit_response/<int:response_id>',
         views.response_edit, name='response_edit'),
    path('<slug:slug>/delete_response/<int:response_id>',
         views.response_delete, name='response_delete'),
]
