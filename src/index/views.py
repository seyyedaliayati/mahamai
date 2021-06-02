from index.models import ContactUs
from django.shortcuts import render

from index.forms import ContactUsForm


def index(request):
    return render(request, 'index/index.html')


def about_us(request):
    return render(request, 'index/about_us.html')


def work_us(request):
    return render(request, 'index/work_us.html')
