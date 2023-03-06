from django.urls import path, include
from product import views

urlpatterns = [
    path('', views.user_product),
    path('all/', views.get_all_product),
    path('<int:id>/', views.user_product_detail)
]