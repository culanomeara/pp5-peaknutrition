from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    """
    Create a form for the subscription
    """
    class Meta:
        """
        Display the required fields
        """
        model = Subscription
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        """
        Add Placeholder to form fields
        """
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            # add class to fields
            self.fields[field].widget.attrs['class'] = 'my-2'
