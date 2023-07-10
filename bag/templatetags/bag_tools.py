from django import template


register = template.Library()


# https://stackoverflow.com/questions/39021159/django-template-send-two-arguments-to-template-tag

# @register.simple_tag
# def calc_item_subtotal(price, quantity):
#     # Function for calculating subtotal for each line item in bag


@register.simple_tag
def calc_item_discount_price(price, discount):
    # Function for calculating discount price for each line item in bag
    discount_price = round(price - (price * discount/100), 0)
    return discount_price


@register.simple_tag
def calc_item_subtotal(price, discount, quantity):
    # Function for calculating total cost for each line item in bag
    global tot
    global disc_tot
    tot = 0
    disc_tot = 0

    if discount != 0:
        tot = round(price * quantity, 0)
        disc_tot = round(price * discount/100 * quantity, 0)
    else:
        tot = round(price * quantity, 0)

    item_total = tot - disc_tot
    return item_total


# @register.simple_tag
# def calc_item_total():
#     # Function for calculating subtotal for each line item in bag
#     item_total = 
#     return item_total


@register.simple_tag
def strike(text):
    str_text = str(text)
    result = ''
    for c in str_text:
        result = result + c + '\u0336'
    return result
