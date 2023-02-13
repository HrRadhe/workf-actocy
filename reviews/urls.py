from django.urls import path, include
from . import views

urlpatterns = [ 
    path('',views.check),
    path('c-reviews/',views.c_reviews, name='c_reviews'),
    path('edit-review/<int:pk>/', views.edit_review, name='edit_review'),
    path('c-review-detail/<int:pk>', views.c_review_detail, name='c_review_detail'),

    path('reviews-s/', views.reviews_s, name='reviews_s'),
    path('review-detail-s/<int:pk>/', views.review_detail_s, name='review_detail_s'),
]