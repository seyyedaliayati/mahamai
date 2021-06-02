from django.shortcuts import render


def bootcamp_list(request):
    return render(request, 'bootcamp/bootcamp_list.html')

