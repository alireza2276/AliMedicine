from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:pk>/', views.category, name='category'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
]
