from . import views
from django.urls import path

urlpatterns = [
    path('', views.ThreadList.as_view(), name='threadlist'),
    path('new-thread/', views.new_thread, name='new'),
    path('<slug:slug>/', views.thread_detail, name='thread_detail'),
    path('<slug:slug>/edit_thread/<int:thread_id>',
         views.thread_edit, name='thread_edit'),
    path('<slug:slug>/edit_response/<int:response_id>',
         views.response_edit, name='response_edit'),
    path('<slug:slug>/delete_response/<int:response_id>',
         views.response_delete, name='response_delete'),     
]