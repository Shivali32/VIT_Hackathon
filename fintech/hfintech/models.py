from django.db import models

# Create your models here.
from passlib.hash import pbkdf2_sha256
from django_mysql.models import ListCharField
from django.contrib.auth.models import User

class UserProfile(User):
    user_id = models.CharField(unique=True,db_index=True,max_length = 10)
    contact_number = models.CharField(max_length=10)
    name = models.CharField(max_length = 200)
    #username = models.CharField(max_length=200,unique=True)
    email_id = models.CharField(max_length=200, unique = True)

    bpoints_balance = models.FloatField()

    def str(self):
        return self.email_id



class Company(models.Model):
    company_id = models.CharField(max_length = 10, unique = True)
    company_name = models.CharField(max_length = 100,unique= True)
    def str(self):
        return self.company_name
    

class StockPrice(models.Model):

    company_id = models.ForeignKey(Company, on_delete = models.CASCADE)

    current_stock_price = models.FloatField(default = 0)

    day_value = models.IntegerField()

    def str(self):
        return self.company_id.company_name + str(self.day_value)+ str(self.current_stock_price)


class Investment(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE)

    comapny_id = models.ForeignKey(Company, on_delete = models.CASCADE)
    
    quantity  =  models.IntegerField(default=0)

    average_buy_cost = models.FloatField(default = 0)


    def str(self):
        return self.user_id

class Transactions(models.Model):

    transaction_name = models.CharField(max_length = 50)

    transaction_id = models.CharField(db_index = True, max_length = 10,unique=True)

    user_id = models.ForeignKey(UserProfile,on_delete=models.CASCADE) 

    bpoints = models.FloatField()

    inr_spent = models.FloatField()

    credit = models.IntegerField()


    def str(self):
        return self.transaction_name + str(self.bpoints) + str(self.credit)




