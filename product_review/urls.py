from django.urls import path
from .import views

urlpatterns = [
    path('', views.reveal_reviews, name='product_review'),
    path('add_product_review/<int:product_id>/', views.add_product_review,
         name='add_product_review'),
    path('edit_product_review/<int:review_id>/',
         views.edit_product_review,
         name='edit_product_review'),
    path('delete_review/<int:review_id>/',
         views.delete_review,
         name='delete_review'),
]
