from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Account,Card,Machine,Transaction

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Machine)
admin.site.register(Transaction)
