import jdatetime
import locale

from django import template

register = template.Library()


@register.filter(name="farsi_date")
def farsi_date(value):
    jdatetime.set_locale("fa_IR")
    jdate = jdatetime.datetime.fromgregorian(date=value)
    return jdate.strftime("%a، %d %b %Y")
