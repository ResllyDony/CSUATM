from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Account,Card,Machine,Transaction

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Account)
admin.site.register(Card)
#admin.site.register(Machine)
admin.site.register(Transaction)

class MachineAdmin(admin.ModelAdmin):
    list_display = ('current_balance','minimum_balance','location','last_refill','next_maintenance_date')
    

admin.site.register(Machine,MachineAdmin)
