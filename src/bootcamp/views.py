from django.http import HttpResponse
from django.shortcuts import render

from .forms import BootCampRegisterForm
from .selectors import get_all_bootcamps, get_bootcamp_by_pk, get_bootcamp_register_by_pk
from .utils import make_payment, verify_payment


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
            return make_payment(request, obj)
        else:
            print("Errors")

    return render(request, 'bootcamp/bootcamp_register.html', context=context)


def bootcamp_register_verify(request, pk):
    register = get_bootcamp_register_by_pk(pk)
    if request.GET.get('Status') == 'OK':
        return verify_payment(request, register)
    else:
        return HttpResponse('Transaction failed or canceled by user')
