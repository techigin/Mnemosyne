# Generated by Django 2.1.7 on 2019-05-12 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_transactions_transactions_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='reconcile',
        ),
    ]
