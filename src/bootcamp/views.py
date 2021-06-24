from django.shortcuts import render
from django.urls import reverse

from .selectors import get_all_bootcamps

# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client

MERCHANT = 'ee262516-f313-4e1d-bad0-a12e0d1f03c5'
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'ghaem.saadatjo@gmail.com'  # Optional
mobile = '09123456789'  # Optional

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
