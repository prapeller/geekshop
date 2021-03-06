# Generated by Django 3.2.7 on 2021-09-22 12:46

from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, upload_to='product_images')),
                ('description', models.TextField(blank=True)),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[('USD', '$'), ('EUR', '€'), ('RUB', '₽')], default='₽', editable=False, max_length=3)),
                ('price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='₽', max_digits=8)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory')),
            ],
        ),
    ]
