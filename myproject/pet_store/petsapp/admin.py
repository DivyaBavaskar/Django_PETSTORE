from django.contrib import admin
from .models import Pet
# from .models import Pet,Order,OrderItem,Customer,ShippingAddress

# Register your models here.

# admin.site.register(Pet)
class PetAdmin(admin.ModelAdmin): 
    list_display=('id','name','gender','breed','description')
admin.site.register(Pet,PetAdmin)

# class OrderAdmin(admin.ModelAdmin):
#     list_display=('customer','date_ordered','complete','transaction_id')
# admin.site.register(Order,OrderAdmin)
# admin.site.register(OrderItem)
# admin.site.register(Customer)
# admin.site.register(ShippingAddress)

