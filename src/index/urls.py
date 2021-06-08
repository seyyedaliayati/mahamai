from django.urls import path

from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about_us'),
    path('work-with-us/', views.work_us, name='work_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
]
