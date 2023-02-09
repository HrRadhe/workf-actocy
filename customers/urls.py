from django.urls import path, include
from . import views
from accounts.views import customerDashboard as CD
urlpatterns = [ 

    path('',CD),
    path('profile/', views.c_editprofile, name="c_editprofile"),
    path('pending-order/<int:pk>/', views.pending_order, name='pending_order'),
    path('all-booking/', views.all_booking, name="all_booking"),
    path('cancel_order/<int:pk>/', views.cancel_order, name='cancel_order'),
    path('c-delete-profile', views.c_delete_profile, name='c_delete_profile'),
    path('order-detail/<int:pk>', views.order_detail, name='order_detail'),
]