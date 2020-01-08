from django.contrib import admin
from .models import Transactions, Legend, Profile

# Register your models here.
admin.site.register(Transactions)
admin.site.register(Legend)
admin.site.register(Profile)
