from django.contrib import admin
from .models import Product, Category, Type


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'type',
        'price',
        'featured_image',
        'tags',
    )

    ordering = ('type',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
