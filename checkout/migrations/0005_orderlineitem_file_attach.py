# Generated by Django 3.2.19 on 2023-06-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_alter_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='file_attach',
            field=models.FileField(default='40501-1_duck.jpeg', upload_to=''),
            preserve_default=False,
        ),
    ]
