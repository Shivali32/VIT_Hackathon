from django.contrib import admin
from hfintech.models import UserProfile,Company, StockPrice, Investment,Transactions,BitsTransaction

admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(StockPrice)
admin.site.register(Investment)
admin.site.register(Transactions)
admin.site.register(BitsTransaction)


# Register your models here.
