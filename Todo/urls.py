from django.contrib import admin
from django.urls import path 
from .import views

urlpatterns = [
    
    path('', views.home,name="home"),
    path('add_todo/' , views.add_Todo , name="add_todo"),
    path('view_todo/' , views.view_Todo , name="view_todo"),
    path('signup/' , views.sign_up , name="signup"),
    path('loginpage/' , views.loginpage , name="loginpage"),
    path('logout/' , views.logoutpage , name="logout"),
    path('updatestatus/<int:pk>' , views.updatestatus , name="updatestatus"),
    path('view_todo_details/<int:pk>' , views.view_todo_details , name="view_todo_details"),
    path('edit_todo/<int:pk>/' , views.edit_todo , name="edit_todo"),
    path('delete_todo/<int:pk>/' , views.delete_todo , name="delete_todo"),

]