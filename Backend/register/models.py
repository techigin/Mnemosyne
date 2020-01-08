from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .signals import calculate_current_balance_signal

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=000.00)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Transactions(models.Model):
    code = models.CharField(max_length=3)
    date =  models.DateField(auto_now=False, auto_now_add=False)
    transactions_description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=000.00)
    transactions_type = models.TextField(max_length=6, default=None)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )


    def __str__(self):
        return self.code


class Legend(models.Model):
    code = models.CharField(max_length=3)
    transactions_category = models.CharField(max_length=50)
    transactions_type = models.TextField(max_length=6)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.code
