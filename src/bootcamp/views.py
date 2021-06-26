from django.shortcuts import render
from django.urls import reverse

from .forms import BootCampRegisterForm
from .selectors import get_all_bootcamps, get_bootcamp_by_pk
from .utils import make_payment

# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client



client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
CallbackURL = 'http://localhost:8001/bootcamp/verify'  # Important: need to edit for realy server.


def send_request(request):
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            # return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
            return render(request, 'index/thanks.html', context={'message': 'از خرید شما سپاس گزاریم!'})
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')


def bootcamp_list(request):
    bootcamps = get_all_bootcamps()
    context = {
        'bootcamp_list': bootcamps,
    }
    return render(request, 'bootcamp/bootcamp_list.html', context=context)


def bootcamp_detail(request, pk):
    bootcamp = get_bootcamp_by_pk(pk)
    context = {
        'bootcamp': bootcamp,
    }
    return render(request, 'bootcamp/bootcamp_detail.html', context=context)


def bootcamp_register(request, pk):
    bootcamp = get_bootcamp_by_pk(pk)
    context = {
        'bootcamp': bootcamp,
    }
    if request.method == "POST":
        form = BootCampRegisterForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.bootcamp = bootcamp
            obj.save()
            return make_payment(obj)
        else:
            print("Errors")

    return render(request, 'bootcamp/bootcamp_register.html', context=context)

