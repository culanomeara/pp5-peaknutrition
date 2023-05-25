from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# Q: Special Object from django.db to help us get a search query
from django.db.models import Q
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'srchq' in request.GET:
            query = request.GET['srchq']
            if not query:
                messages.error(request, "You need to enter something!")
                return redirect(reverse('products'))
            # i here makes it case-insensitive
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
