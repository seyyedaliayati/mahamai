from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.bootcamp_list, name='bootcamp_list'),
    path('detail/<int:pk>/', views.bootcamp_detail, name='bootcamp_detail'),
    path('register/<int:pk>/', views.bootcamp_register, name='bootcamp_register'),
    path('register/verify/<int:pk>/', views.bootcamp_register_verify, name='bootcamp_register_verify'),
]
