from index.models import ContactUs
from django.shortcuts import render
from django.http import HttpResponseForbidden

from index.forms import ContactUsForm


def index(request):
    return render(request, 'index/index.html')


def about_us(request):
    return render(request, 'index/about_us.html')


def work_us(request):
    return render(request, 'index/work_us.html')


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index/index.html', {'thanks': True})
        else:
            print(form.errors)
            return render(request, 'index/index.html', {'error': True})
    return HttpResponseForbidden()
