from django.urls import path , include
from . import views

urlpatterns = [
    
    path('profile/', views.s_editprofile, name="s_editprofie"),
    path('delete-profile/', views.deleteprofile, name="delete-profile"),
    path('my-service', views.my_service, name='my_service'),


]