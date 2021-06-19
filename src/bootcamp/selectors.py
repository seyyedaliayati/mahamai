
from .models import BootCamp


def get_all_bootcamps():
    return BootCamp.objects.all()
