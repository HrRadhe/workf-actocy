from django.urls import path, include
from . import views

urlpatterns = [ 

    path('checkout/<int:pk>', views.checkout, name='checkout'),
    path('place-order', views.place_order, name='place_order'),
]