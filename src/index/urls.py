from django.urls import path

from index.views import IndexView, ContactUsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
]
