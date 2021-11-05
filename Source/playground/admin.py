from django.contrib import admin

# Register your models here.
from .models import Card, Transaction, Machine, Account

admin.site.register(Card)
admin.site.register(Transaction)
admin.site.register(Machine)
admin.site.register(Account)
