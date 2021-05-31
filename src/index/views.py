from django.views import generic

from index.forms import ContactUsForm


class IndexView(generic.TemplateView):
    template_name = 'index/index.html'


class ContactUsView(generic.FormView):
    template_name = 'index/contact_us.html'
    form_class = ContactUsForm
