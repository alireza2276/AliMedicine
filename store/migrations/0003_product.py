# Generated by Django 5.0.1 on 2024-01-25 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_category_parent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('price', models.PositiveBigIntegerField(verbose_name='price')),
                ('discount', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='discount')),
                ('image', models.ImageField(upload_to='static/product-image', verbose_name='image')),
                ('inventory', models.IntegerField()),
                ('expire', models.CharField(blank=True, max_length=255, null=True, verbose_name='expire')),
                ('description', models.TextField(verbose_name='description')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='short_description')),
                ('country_created', models.CharField(blank=True, max_length=255, null=True, verbose_name='country_created')),
                ('volume', models.CharField(blank=True, max_length=255, null=True, verbose_name='volume')),
                ('gender', models.CharField(blank=True, max_length=255, null=True, verbose_name='gender')),
                ('number', models.CharField(blank=True, max_length=255, null=True, verbose_name='number')),
                ('length', models.CharField(blank=True, max_length=255, null=True, verbose_name='length')),
                ('compounds', models.TextField(blank=True, null=True, verbose_name='compounds')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modeified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='category')),
            ],
        ),
    ]