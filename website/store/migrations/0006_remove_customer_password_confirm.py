# Generated by Django 4.2.7 on 2023-11-22 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_customer_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password_confirm',
        ),
    ]
