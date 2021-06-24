from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.bootcamp_list, name='bootcamp_list'),
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
]
