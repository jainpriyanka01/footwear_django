# Generated by Django 3.0.5 on 2020-08-11 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20200810_0340'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductColorImages',
            new_name='ProductColorImage',
        ),
    ]