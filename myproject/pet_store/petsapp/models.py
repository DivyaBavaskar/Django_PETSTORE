from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pet(models.Model):
    gender=(('male','male'),('female','female'))
    image=models.ImageField(upload_to='media')
    name=models.CharField(max_length=150)
    breed=models.CharField(max_length=150)
    gender=models.CharField(max_length=30,choices=gender)
    description = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    

class Customer1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default='NA')

    def str(self):
        return self.user.username


class Cartitem(models.Model):
    customer = models.ForeignKey(Customer1, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'cart_items'

    def __str__(self):
        return self.pet.name 

class ShippingAddress1(models.Model):
    customer=models.ForeignKey(Customer1,on_delete=models.CASCADE,null=True)
    building_name=models.CharField(max_length=300,null=False,blank=False)
    street=models.CharField(max_length=200,blank=True)
    landmark=models.CharField(max_length=200,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    state=models.CharField(max_length=30,null=False)
    zipcode=models.CharField(max_length=8,null=False)
    date_added=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    customer=models.ForeignKey(Customer1,on_delete=models.SET_NULL,null=True)
    date_ordered =models.DateTimeField(auto_now_add=True)
    compltete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100,null=True)
    shipping_address = models.ForeignKey(ShippingAddress1,on_delete=models.CASCADE,null = True)

    def __str__(self) :
        return str(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    product= models.ForeignKey(Pet,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,related_name='items',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=9,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def get_cost(self):
        return self.price * self.quantity









