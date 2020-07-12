from django.contrib import admin

# Register your models here.
from .models import Time,Symbols,Symbols_Transactions

admin.site.register(Time)
admin.site.register(Symbols)
admin.site.register(Symbols_Transactions)
