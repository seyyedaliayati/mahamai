from index.models import ContactUs
from django.shortcuts import render

from index.forms import ContactUsForm


def index(request):
    return render(request, 'index/index.html')
