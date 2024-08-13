from pyexpat import model
from tkinter import CASCADE
from django.db import models


# from HungrezyApp.views import contact
from django.contrib.auth.models import User

# Create your models here.

class admin(models.Model):
    a_id = models.IntegerField(primary_key = True)
    address = models.TextField()
    contact_number = models.CharField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

# class customer(models.Model):
#     cus_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=30)
#     address = models.TextField()
#     contact_number = models.CharField(max_length=11)
#     gender = models.CharField(max_length=10)
#     password = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    # password = models.CharField(max_length=30)
    
class customer_account(models.Model):
    cus_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.TextField()
    contact_number = models.CharField(max_length=11)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class restaurant_or_homemade_food(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.TextField()
    contact_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=30)
    types = models.CharField(max_length=10)
    rating = models.FloatField()
    review = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
# class home_made_food(models.Model):
#     hmf_suppiler_id = models.IntegerField(primary_key=True)
    
class order(models.Model):
    o_id = models.IntegerField(primary_key=True)
    number_of_servings = models.IntegerField()
    total_amount = models.IntegerField()
    date = models.DateField()
    
class order_item(models.Model):
    order_item_id = models.IntegerField(primary_key=True)
    menu = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    o_id = models.ForeignKey(order, on_delete=models.CASCADE)

class menu(models.Model):
    item_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    
# class rider(models.Model):
#     rid_id = models.IntegerField(primary_key=True)
#     u_name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=30)
#     address = models.TextField()
#     delivary_method = models.CharField(max_length=10)
#     gender = models.CharField(max_length=10)
#     contact_number = models.CharField(max_length=11)
#     password = models.CharField(max_length=20)
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
    
class business_account(models.Model):
    bus_acc_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    res_name = models.CharField(max_length=30)
    service = models.CharField(max_length=20)
    # food_type = models.CharField(max_length=20)
    address = models.TextField()
    contact_no = models.CharField(max_length=11)
    # gender = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class rider_account(models.Model):
    rid_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.TextField()
    delivary_method = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=11)
    password = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)