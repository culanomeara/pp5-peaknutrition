from django import template


register = template.Library()


# https://stackoverflow.com/questions/39021159/django-template-send-two-arguments-to-template-tag
@register.simple_tag
def calc_subtotal(price, quantity):
    global tot
    tot = round(price * quantity, 0)
    return tot


@register.simple_tag
def calc_discount_price(price, discount):
    discount_price = round(price - (price * discount/100), 0)
    return discount_price


@register.simple_tag
def calc_discount_subtotal(price, discount, quantity):
    global disc_tot
    disc_tot = round(price * discount/100 * quantity, 0)
    return disc_tot


@register.simple_tag
def calc_item_total():
    item_total = tot - disc_tot
    return item_total


@register.simple_tag
def strike(text):
    str_text = str(text)
    result = ''
    for c in str_text:
        result = result + c + '\u0336'
    return result