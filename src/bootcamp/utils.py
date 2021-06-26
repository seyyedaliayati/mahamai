from zeep import Client

from django.shortcuts import redirect
from django.http import HttpResponse

MERCHANT_ID = 'ee262516-f313-4e1d-bad0-a12e0d1f03c5'


def make_payment(request, bootcamp_register_obj):
    description = "هزینه ثبت نام در بوت کمپ"  # Required
    email = bootcamp_register_obj.email
    mobile = bootcamp_register_obj.phone
    callback_url = request.build_absolute_uri('/')[:-1] + bootcamp_register_obj.get_callback_url()
    client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
    result = client.service.PaymentRequest(MERCHANT_ID, bootcamp_register_obj.bootcamp.price, description, email, mobile, callback_url)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


def verify_payment(request, register):
    client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
    result = client.service.PaymentVerification(MERCHANT_ID, request.GET['Authority'], register.bootcamp.price)
    if result.Status == 100:
        return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        # return render(request, 'index/thanks.html', context={'message': 'از خرید شما سپاس گزاریم!'})
    elif result.Status == 101:
        return HttpResponse('Transaction submitted : ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
