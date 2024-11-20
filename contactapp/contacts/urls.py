from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home , name="home"),
    path('add_contact/' , views.add_contact , name="add_contact"),
    path('view_contact/', views.view_contacts , name="view_contact"),
    path('view_details/<int:pk>', views.view_details , name="view_details"),
    path('edit_contact/<int:pk>/', views.edit_contact , name="edit_contact"),
    #path('status/' , views.status , name="status"),
    path('updatestatus/<int:pk>' , views.updatestatus , name="updatestatus"),
]
