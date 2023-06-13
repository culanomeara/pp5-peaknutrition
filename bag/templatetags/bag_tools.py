from django import template


register = template.Library()


# https://stackoverflow.com/questions/39021159/django-template-send-two-arguments-to-template-tag
@register.simple_tag
def calc_subtotal(price, quantity):
    tot = price * quantity
    return tot


@register.simple_tag
def calc_discount_subtotal(price, discount, quantity):
    disc_tot = price * discount/100 * quantity
    return disc_tot
