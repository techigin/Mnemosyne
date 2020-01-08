from django.forms import ModelForm, DateInput, Select, ModelChoiceField
from .models import Transactions, Legend

class Trans_form(ModelForm):

    class Meta:
        model = Transactions
        fields = [
            'code',
            'date',
            'transactions_description',
            'amount',
            
        ]

        widgets = {
            'date': DateInput(attrs={'class':"datepicker"}),
        }


class Legend_Form(ModelForm):
    class Meta:
        model = Legend
        fields = [
            'code',
            'transactions_category',
            'transactions_type',
        ]
