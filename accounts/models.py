from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=50,null=True,blank=True)
    mobile = models.BigIntegerField(null=True,blank=True)
    location = models.CharField(max_length=50,null=True,blank=True)
    #date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

class Products(models.Model):
    CATAGORY_CHOICE = (
        ('Indoor','Indoor'),
        ('Outoor','Outoor'),
        ('Anywhere','Anywhere')
    )
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    order_date = models.DateField(auto_now=True)
    category = models.CharField(choices=CATAGORY_CHOICE,max_length=100)

    def __str__(self):
        return self.name

class Orders(models.Model):
    STATUS_CHOICES = (
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
        ('OutforDelivery', 'OutforDelivery')
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES,max_length=100)
    created_date = models.DateField(auto_now=True,null=True)
