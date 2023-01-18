from django.urls import path 
from . import views

urlpatterns = [ 

    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerServiceman/', views.registerServiceman, name="registerServiceman"),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myAccount/', views.myAccount, name='myAccount'),

    path('servicemanDashboard/', views.servicemanDashboard, name='servicemanDashboard'),
    path('customerDashboard/', views.customerDashboard, name='customerDashboard'),

    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
]