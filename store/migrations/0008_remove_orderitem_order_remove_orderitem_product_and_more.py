# Generated by Django 5.0.1 on 2024-01-29 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
