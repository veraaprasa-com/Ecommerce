from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(size_category)
class size_categoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name']

@admin.register(size_option)
class size_optionAdmin(admin.ModelAdmin):
    list_display=['id','size_name','sort_order','size_category_id','slug']

@admin.register(product_category)
class product_category(admin.ModelAdmin):
    list_display=['id','category_name','category_image','category_description','slug']

@admin.register(brand)
class brandAdmin(admin.ModelAdmin):
     list_display=['id','brand_name','brand_description']

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=['id','product_category','product_name','product_description','model_height','about']

@admin.register(colour)
class colourAdmin(admin.ModelAdmin):
    list_display=['id','colour_name']

@admin.register(product_item)
class product_itemAdmin(admin.ModelAdmin):
    list_display=['id','product','colour','original_price','size_category','sale_price','sizeoption','slug']

@admin.register(product_variation)
class product_variation(admin.ModelAdmin):
    list_display=['product_item_id','size_id','qty_in_stock']

@admin.register(product_image)
class product_image(admin.ModelAdmin):
    list_display=['product_item_id','image_filename']

@admin.register(UserModels)
class UserModelAdmin(admin.ModelAdmin):
    list_display=['Fullname','phone','picture','address']

@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=['user','ordered','product_item','quantity','size']

@admin.register(AddressModel)
class AddressModelAdmin(admin.ModelAdmin):
    list_display=['street_address','apartment_address','country','pincode','default']

@admin.register(PaymentModel)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['user','amount','timestamp']
@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display=['user','reference_code','items','startdate','ordered_date','ordered','shipping_adrs',
                  'payment','being_delivered','received','refund_requested','refund_granted']
