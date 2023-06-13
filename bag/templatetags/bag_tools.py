from django import template


register = template.Library()


# https://stackoverflow.com/questions/39021159/django-template-send-two-arguments-to-template-tag
@register.simple_tag
def calc_subtotal(price, quantity):
    global tot
    tot = round(price * quantity, 2)
    return tot


@register.simple_tag
def calc_discount_subtotal(price, discount, quantity):
    global disc_tot
    disc_tot = round(price * discount/100 * quantity, 2)
    return disc_tot


@register.simple_tag
def calc_item_total():
    item_total = tot - disc_tot
    return item_total
