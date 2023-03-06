from django.urls import path, include
from product_review import views

urlpatterns = [
    path('', views.user_product_review),
    path('all/', views.get_all_product_review),
    path('product_id/', views.user_product_review),
    path('<int:product_id>/', views.get_review_by_product_id)
]