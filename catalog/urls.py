from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('balance/',views.checkBalance,name='check'),
    path('account/withdraw/',views.Withdraw,name = 'withdraw'),
    path('account/transfer/',views.Transfer,name = 'transfer'),
    path('account/transfer/noFunds',views.noFunds,name = 'noFunds'),
    path('account/transfer/noAccount',views.noAccount,name = 'noAccount'),
    path('account/transfer/success',views.TransferSuccess,name = 'transferSuccess'),
    path('account/withdraw/failed',views.Failed, name = 'failed'),
    path('account/withdraw/success',views.Success, name = 'success')
    
]
