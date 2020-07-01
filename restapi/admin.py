from django.contrib import admin
from .models import Bank,Branch,BankBranch

# Register your models here.
admin.site.register(Bank)
admin.site.register(Branch)
admin.site.register(BankBranch)
