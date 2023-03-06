from django.urls import path, include
from tip_trick import views

urlpatterns = [
    path('', views.user_tip_trick),
    path('all/', views.get_all_tip_trick),
]