from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import ContactUs, WorkWithUs


def inform_admin(model_name, instance_id):
    send_mail(
        subject=f'New {model_name}',
        message=f'A new {model_name.lower()} instance submitted with id: {instance_id}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_ADMIN, ],
        fail_silently=True,
    )


def inform_client(instance):
    send_mail(
        subject='MahamAI | No Reply',
        message=f'سلام {instance.get_ull_name()} عزیز،' + \
                ' پیام شما با موفقیت به دست ما رسید. کارشناسان مهام به زودی با شما تماس خواهند گرفت. ' + \
                'این یک ایمیل خودکار است لطفا پاسخ ندهید.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[instance.email, ],
        fail_silently=True,
    )


@receiver(post_save, sender=ContactUs)
def inform_via_email(sender, instance, created, **kwargs):
    if created:
        inform_admin("Contact Us", instance.id)
        inform_client(instance)


@receiver(post_save, sender=WorkWithUs)
def inform_via_email(sender, instance, created, **kwargs):
    if created:
        inform_admin("Contact Us", instance.id)
        inform_client(instance)
