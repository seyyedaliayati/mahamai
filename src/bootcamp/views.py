from django.shortcuts import render

from .selectors import get_all_bootcamps


def bootcamp_list(request):
    bootcamps = get_all_bootcamps()
    context = {
        'bootcamp_list': bootcamps,
    }
    return render(request, 'bootcamp/bootcamp_list.html', context=context)

