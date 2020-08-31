# Generated by Django 3.0.5 on 2020-08-31 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0033_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderStatus',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(default='India', max_length=500),
        ),
    ]