# Generated by Django 2.1.7 on 2019-06-19 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20190619_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='legend',
            old_name='user',
            new_name='author',
        ),
    ]