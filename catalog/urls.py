from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('balance/',views.checkBalance,name='check'),
    path('withdraw/',views.Withdraw,name = 'withdraw')
    
]
