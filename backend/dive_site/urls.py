from django.urls import path, include
from dive_site import views

urlpatterns = [
    path('', views.user_dive_sites),
    path('all/', views.get_all_dive_sites),
    path('<int:id>', views.filter_by_id),
]