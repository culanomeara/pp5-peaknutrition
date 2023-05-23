from django.contrib import admin
from .models import Product, Category, Type


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'type'
        'price',
        'rating',
        'featured_image',
        'tags',
    )

    ordering = ('type',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)