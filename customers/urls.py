from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This maps the root URL to the home view
    path('upload/', views.upload_file, name='upload'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
]
