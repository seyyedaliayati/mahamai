from django.urls import path

from bootcamp import views

urlpatterns = [
    path('list/', views.bootcamp_list, name='bootcamp_list'),
]
