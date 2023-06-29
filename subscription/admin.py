from django.contrib import admin
from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    Customizes the display of the model in the admin panel
    """
    list_display = [
        'full_name',
        'email',
    ]
    list_filter = ['full_name', 'email']
    search_fields = ['full_name', 'email']