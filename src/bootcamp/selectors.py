from django.shortcuts import get_object_or_404

from .models import BootCamp, BootCampRegister


def get_all_bootcamps():
    return BootCamp.objects.all()


def get_bootcamp_by_pk(pk: int):
    return get_object_or_404(BootCamp, pk=pk)


def get_bootcamp_register_by_pk(pk: int):
    return get_object_or_404(BootCampRegister, pk=pk)
