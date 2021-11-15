from django.shortcuts import render
from .models import Card,Account,Machine,Transaction
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import WithdrawForm,TransferForm
# Create your views here.

def index(request):
    """ View function for home page of site. """

    # Generate counts of some fo the main objects
    num_accounts = Account.objects.count()  
    num_cards = Card.objects.count()
    num_atms = Machine.objects.count()
    

    context = {
        'num_accounts': num_accounts,
        'num_cards': num_cards,
        'num_atms': num_atms,
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def checkBalance(request):
    #get account balance
    account = Account.objects.get(user=request.user)
    account_balance=account.balance
    

    context = {'account_balance': account_balance}

    return render(request,'checkBalance.html',context=context)

def Withdraw(request):

    if request.method == 'POST':
        form = WithdrawForm(request.POST)

        if form.is_valid():
            account = Account.objects.get(user=request.user)
            account_balance=account.balance - form.cleaned_data['withdrawal_amount']
            if account_balance < 0 :
                return HttpResponseRedirect(reverse('failed') )
            else:
                account.balance = account_balance
                account.save()
                return HttpResponseRedirect(reverse('success') )

    else:
        
        form = WithdrawForm(request.POST)
        context = {
                'form':form
                }
        
    return render(request, 'withdraw.html', context)

def Transfer(request):
    
    if request.method == 'POST':
        form = TransferForm(request.POST)
        
        if form.is_valid():
            account_cd = form.cleaned_data['account_num']
            trans_amount = form.cleaned_data['transfer_amount']
            if Account.objects.filter(acc_num=account_cd).exists() == False:
                return HttpResponseRedirect(reverse('noAccount') )
            else:
                account = Account.objects.get(user=request.user) #get user account
                trans_account= Account.objects.get(acc_num = account_cd)#get transfer account
                if account.balance < trans_amount:
                    return HttpResponseRedirect(reverse('noFunds') )
                else:
                    account.balance = account.balance - trans_amount #take away transfer amount from user
                    trans_account.balance = trans_account.balance + trans_amount
                    account.save()
                    trans_account.save()
                    return HttpResponseRedirect(reverse('transferSuccess') )
        else:
            return HttpResponseRedirect(reverse('failed') )
    else:
        form = TransferForm(request.POST)
        context = {
                'form':form
                }
        
    return render(request, 'transfer.html', context)       
            
    
    
def Failed(request):

    return render(request,'failed.html')


def Success(request):
    return render(request,'success.html')

def TransferSuccess(request):
    return render(request,'transferSuccess.html')
def noAccount(request):
    return render(request,'noAccount.html')

def noFunds(request):
    return render(request,'noTransferFunds.html')
