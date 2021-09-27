from django.db import models

# Create your models here.

class Users(models.Model) :

    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    current_address = models.CharField(max_length=200)
    permanent_address = models.CharField(max_length=200)
    nid_no = models.CharField(max_length=100)
    deposit_amount = models.FloatField()
    tenure = models.FloatField()
    opening_date = models.DateField()
    photoFileName = models.CharField(max_length=100)


class Loan(models.Model) :
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    total_balance = models.FloatField()
    is_loan = models.BooleanField()
    loan_amount = models.FloatField()
    tenure = models.FloatField()
    interest_rate = models.FloatField()
