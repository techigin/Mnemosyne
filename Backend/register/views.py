from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelChoiceField
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from .models import Transactions, Legend, Profile
from django.views import View
from django.db.models import Q
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from register.mixins import CalculateCurrentBalanceMixins
from . import forms

import sys

# Create your views here.

'''
This Register View class allow a user to input and view all transactions of that user
'''
class TransactionListView(CalculateCurrentBalanceMixins, View):

    def get(self, request):
        #gets the User's ID from the request object
        user_id = request.user.id
        #query for all transactons make by the user
        transactions = Transactions.objects.filter(author=user_id)
        legend = Legend.objects.filter(author=user_id)
        #gets the profile of the user
        profile = Profile.objects.get(user=user_id)
        #the user balance that is in the profile
        bal = profile.balance

        form = forms.Trans_form()
        queryset=Legend.objects.filter(author=user_id)
        form.fields['code'] = ModelChoiceField(queryset,to_field_name="code")
        context = {
            'transactions' : transactions,
            'legend': legend,
            'form': form,
            'profile': profile,
            'bal': bal
        }
        return render(request, 'register/index.html', context)

    def post(self, request):
        # Instance of Transaction Form
        form = forms.Trans_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            trans_code_form_input = instance.code
            user_id = request.user.id

            code_query = Legend.objects.get(Q(code='abc') & Q(author=1)).transactions_type
            instance.author = request.user
            instance.transactions_type = str(code_query)
            instance.save()
            return redirect('register:trans_list')
        else:
            return redirect('register:trans_list')

class TransactionDeleteView(View):
    def get(self, request, id=None):
        trans_object = get_object_or_404(Transactions, id=id)
        trans_object.delete()
        #message.sucess(request, "Sucessfully deleted")
        return redirect('register:trans_list')

class LegendCodeListView(View):
    def get(self, request):
        form = forms.Legend_Form()
        user_id = request.user.id
        legend = Legend.objects.filter(author=user_id)
        context = {
            'legend': legend,
            'form': form,
        }
        print(request)
        return render(request, 'register/legend.html', context)

    def post(self, request):
        print(request.body)
        form = forms.Legend_Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('register:legend_code_list')

class LegendCodeDeleteView(View):
    def get(self, request, id=None):
        legend_object = get_object_or_404(Legend, id=id)
        legend_object.delete()
        return redirect('register:legend_code_list')

@receiver(pre_delete, sender=Transactions)
def update_balance_delete(sender, instance, **kwards):
    trans = Transactions.objects.get(id=instance.id)
    trans_type = trans.transactions_type

    user = instance.author
    profile_bal = Profile.objects.get(user=user).balance
    trans_amount = trans.amount

    if trans_type == 'debit':
        updated_bal = profile_bal + trans_amount
    else:
        updated_bal = profile_bal - trans_amount
    current_bal = Profile.objects.filter(user=user).update(balance=updated_bal)

@receiver(post_save, sender=Transactions)
def update_balance_add(sender, instance, **kwards):
    trans = Transactions.objects.get(id=instance.id)
    trans_type = trans.transactions_type

    user = instance.author
    profile_bal = Profile.objects.get(user=user).balance
    trans_amount = trans.amount

    if trans_type == 'debit':
        updated_bal = profile_bal - trans_amount
    else:
        updated_bal = profile_bal + trans_amount
    current_bal = Profile.objects.filter(user=user).update(balance=updated_bal)
