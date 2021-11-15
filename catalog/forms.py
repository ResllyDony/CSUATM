
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django import forms
from .models import Account


class WithdrawForm(forms.Form):
    
    withdrawal_amount = forms.IntegerField(label = 'Enter an amount to withdraw')

    def clean_withdrawal_amount(self):
        data = self.cleaned_data['withdrawal_amount']

        if data <=0:
            raise ValidationError(_('Invalid entry, must be greater than 0'))

        return data
    
class TransferForm(forms.Form):
    account_num = forms.FloatField(label = 'Enter an account number to Transfer to')
    transfer_amount = forms.FloatField(label='Enter amount to transfer')

    def clean_account_num(self):
        data = self.cleaned_data['account_num']
        

        return data

    def clean_transfer_amount(self):
        data = self.cleaned_data['transfer_amount']
        if data <=0 :
            raise ValidationError(_('Invalid entry, must be greater than 0'))
        return data
