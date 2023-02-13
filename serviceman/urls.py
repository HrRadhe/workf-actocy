from django.urls import path , include
from . import views
from accounts.views import servicemanDashboard as SD

urlpatterns = [

    path('',SD),
    path('profile/', views.s_editprofile, name="s_editprofie"),
    path('delete-profile/', views.deleteprofile, name="delete-profile"),
    path('my-service/', views.my_service, name='my_service'),
    path('s-pending-booking/<int:pk>/', views.s_pending_booking, name='s_pending_booking'),
    path('all-booking-s/',views.all_booking_s, name='all_booking_s'),
    path('order-detail-s/<int:pk>', views.order_detail_s, name='order_detail_s'),
    path('wallet/',include('wallet.urls')),
]