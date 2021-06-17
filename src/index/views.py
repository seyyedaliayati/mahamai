from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponse

from .models import ContactUs
from .forms import ContactUsForm, WorkWithUsForm


def index(request):
    return render(request, 'index/index.html')


def about_us(request):
    return render(request, 'index/about_us.html')


def work_us(request):
    if request.method == "POST":
        form = WorkWithUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    return render(request, 'index/work_us.html')


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            print(form.errors)
    return HttpResponseForbidden()


def thanks(request):
    message = "اطلاعات شما با موفقیت دریافت شد! متخصصان ما به زودی با شما تماس خواهند گرفت!"
    context = {
        'message': message,
    }
    return render(request, 'index/thanks.html', context)
