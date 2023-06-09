from django.contrib import admin
from .models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    """
    Customizes the display of the model in the admin panel
    """
    list_display = [
        'sent_date',
        'full_name',
        'email',
        'subject',
        'newsletter',
    ]
    list_filter = ['newsletter', 'sent_date']
    search_fields = ['first_name', 'last_name', 'email', 'subject']
