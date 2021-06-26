
def make_payment(bootcamp_register_obj):
    # TODO: Complete stable payment
    MERCHANT = 'ee262516-f313-4e1d-bad0-a12e0d1f03c5'
    amount = 1000  # Toman / Required
    description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
    email = 'ghaem.saadatjo@gmail.com'  # Optional
    mobile = '09123456789'  # Optional

    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))