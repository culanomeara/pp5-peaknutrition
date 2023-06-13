from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    discount_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        discount_total += quantity * product.price*product.discount/100
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    grand_total = total - discount_total
    print({total}, {discount_total}, {grand_total})
    context = {
        'bag_items': bag_items,
        'total': total,
        'discount_total': discount_total,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context
