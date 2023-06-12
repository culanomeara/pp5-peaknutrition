from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


# @register.filter(name='calc_discount_subtotal')
# def calc_discount_subtotal(price, discount, quantity):
#     return price * discount/100 * quantity
