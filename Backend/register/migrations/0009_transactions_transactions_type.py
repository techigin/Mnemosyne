# Generated by Django 2.1.7 on 2019-05-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20190511_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='transactions_type',
            field=models.TextField(default=None, max_length=6),
        ),
    ]
