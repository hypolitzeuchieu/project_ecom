# Generated by Django 4.2.7 on 2023-11-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_customer_name_alter_customer_email_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
