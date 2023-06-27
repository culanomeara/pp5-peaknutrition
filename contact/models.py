from django.db import models
from datetime import date


class ContactForm(models.Model):
    """
    Model to store info about contact form submitted by a user.
    """
    full_name = models.CharField(max_length=50, verbose_name="Full Name*")
    email = models.EmailField(max_length=254, verbose_name="Email*")
    subject = models.CharField(max_length=100, verbose_name="Subject*")
    message = models.TextField(verbose_name="Message*")
    newsletter = models.BooleanField(
        default=False, verbose_name="Subscribe to newsletter")
    sent_date = models.DateField(auto_now_add=True, verbose_name="Sent Date")

    class Meta:
        ordering = ['-sent_date']

    def __str__(self):
        return (
            f"{self.full_name}"
        )
