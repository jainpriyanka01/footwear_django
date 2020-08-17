# Generated by Django 3.0.5 on 2020-08-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20200814_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Out For Delivery', 'Out For Delivery'), ('In Progress', 'In Progress')], default='In Progress', max_length=100),
        ),
    ]