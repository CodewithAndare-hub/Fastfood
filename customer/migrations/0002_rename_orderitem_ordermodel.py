# Generated by Django 5.0.6 on 2024-05-26 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='OrderModel',
        ),
    ]
