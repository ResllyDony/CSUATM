from django.shortcuts import render
from .models import Card,Account,Machine,Transaction

# Create your views here.

def index(request):
    """ View function for home page of site. """

    # Generate counts of some fo the main objects
    num_accounts = Account.objects.count()  
    num_cards = Card.objects.count()
    num_atms = Machine.objects.count()
    num_transactions = Transaction.objects.count()

    context = {
        'num_accounts': num_accounts,
        'num_cards': num_cards,
        'num_atms': num_atms,
        'num_transactions': num_transactions,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def checkBalance(request):
    #get account balance
    account = Account.objects.get(user=request.user)
    account_balance=account.balance
    

    context = {'account_balance': account_balance}

    return render(request,'checkBalance.html',context=context)

def withdraw(request):
    
