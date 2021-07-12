from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

#model Regestration
from .models import(
    customer,
    Product,
    cart,
    orderPlaced,
    ProductReiew
)

@admin.register(customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','description','category','product_image']

@admin.register(cart)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(orderPlaced)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','order_date','status']

@admin.register(ProductReiew)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','product','user']