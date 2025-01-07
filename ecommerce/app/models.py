from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
import uuid
# Create your models here.
class size_category(models.Model):
    category_name=models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class size_option(models.Model):
    size_name=models.CharField(max_length=100)
    sort_order=models.CharField(max_length=100)
    size_category_id=models.ForeignKey(size_category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.size_name
    def save(self,*args,**kwargs):
        self.slug=(str(self.size_category_id)+' '+self.size_name).replace(' ','-')
        super().save(*args,**kwargs)
    
class product_category(models.Model):
    category_name=models.CharField(max_length=100)
    category_image=models.ImageField(upload_to='product_category/',blank=True,null=True)
    category_description=models.TextField(max_length=1000)
    slug=models.CharField(max_length=100,null=True,blank=True)
    parent_category=models.ForeignKey('product_category',on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.category_name
    def save(self,*args,**kwargs):
        self.slug=str(self.category_name).replace(' ','-')
        super().save(*args,**kwargs)
    
class brand(models.Model):
    brand_name=models.CharField(max_length=100)
    brand_description=models.TextField(max_length=1000)
    def __str__(self):
        return self.brand_name
    
class product(models.Model):
    product_category=models.ForeignKey(product_category,on_delete=models.CASCADE)
    brand_id=models.ForeignKey(brand,on_delete=models.CASCADE,blank=True,null=True)
    product_name=models.CharField(max_length=100)
    product_description=models.TextField(max_length=1000)
    model_height=models.CharField(max_length=100,blank=True,null=True)
    model_wearing=models.CharField(max_length=100,blank=True,null=True)
    care_instructions=models.CharField(max_length=100,blank=True,null=True)
    slug=models.CharField(max_length=100,null=True,blank=True)
    about=models.TextField(max_length=1000,blank=True,null=True)
    def __str__(self):
        return self.product_name

class colour(models.Model):
    colour_name=models.CharField(max_length=100)
    def __str__(self):
        return self.colour_name

class product_item(models.Model):
    # product_item_id=models.AutoField(primary_key=True,null=False,blank=False)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    colour=models.ForeignKey(colour,on_delete=models.CASCADE)
    original_price=models.IntegerField()
    size_category=models.ForeignKey(size_category,on_delete=models.SET_NULL,null=True,blank=True)
    sizeoption=models.ForeignKey(size_option,on_delete=models.SET_NULL,null=True,blank=True)
    sale_price=models.IntegerField()
    slug=models.CharField(max_length=100,null=True,blank=True)
    product_code =models.CharField(max_length=100,null=True,blank=True)
    image1=models.ImageField(upload_to='product_image/',blank=True,null=True)
    image2=models.ImageField(upload_to='product_image/',blank=True,null=True)
    image3=models.ImageField(upload_to='product_image/',blank=True,null=True)
    image4=models.ImageField(upload_to='product_image/',blank=True,null=True)
    def __str__(self):
        return str(self.product)
    def save(self,*args,**kwargs):
        self.slug=str(self.product.product_category)+'-'+str(self.product)+'-'+str(self.colour).replace('','-')
        super().save(*args,**kwargs)
    
class product_variation(models.Model):
    product_item_id=models.ForeignKey(product_item,on_delete=models.CASCADE)
    size_id=models.ForeignKey(size_option,on_delete=models.CASCADE)
    qty_in_stock=models.IntegerField()
    def __int__(self):
        return self.product_item_id

class product_image(models.Model):
    product_item_id=models.ForeignKey(product_item,on_delete=models.CASCADE)
    image_filename=models.TextField(max_length=100)
    def __int__(self):
        return self.product_item_id

gen=[['male','Male'],['female','Female']]
class UserModels(User):
    userid=models.AutoField(primary_key=True)
    Fullname=models.CharField(max_length=100)
    phone=models.IntegerField(null=True)
    picture=models.ImageField(upload_to='profile_picture/',blank=True,null=True)
    address=models.CharField(max_length=500,null=True,blank=True)
    gender=models.CharField(max_length=10,choices=gen,blank=True,null=True)
    def __str__(self):
        return self.Fullname

class OrderItemModel(models.Model):
    user=models.ForeignKey(UserModels,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    product_item=models.ForeignKey(product_item,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    size=models.ForeignKey(size_option,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.user)

class AddressModel(models.Model):
    user=models.ForeignKey(UserModels,on_delete=models.CASCADE)
    street_address=models.CharField(max_length=100,null=False)
    apartment_address=models.CharField(max_length=100,blank=True,null=True)
    country=CountryField(multiple=False,null=False)
    pincode=models.CharField(max_length=100,null=False)
    address_type=models.CharField(max_length=1,choices=[('B','Billing'),('S','Shipping')],null=False,blank=False)
    default=models.BooleanField(default=False,null=False)
    def __str__(self):
        return str(self.user)

class PaymentModel(models.Model):
    user=models.ForeignKey(UserModels,on_delete=models.CASCADE)
    amount=models.DecimalField(decimal_places=2,max_digits=2)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)

class OrderModel(models.Model):
    user=models.ForeignKey(UserModels,on_delete=models.CASCADE)
    reference_code=models.CharField(max_length=100,null=True,blank=True)
    items=models.ForeignKey(OrderItemModel,on_delete=models.CASCADE)
    startdate=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField(blank=True,null=True)
    ordered=models.BooleanField(default=False,null=True,blank=True)
    shipping_adrs=models.ForeignKey(AddressModel,related_name='Shipping',on_delete=models.CASCADE,null=True,blank=True)
    bill_adrs=models.ForeignKey(AddressModel,related_name='Billing',on_delete=models.CASCADE,null=True,blank=True)
    payment=models.ForeignKey(PaymentModel,on_delete=models.CASCADE)
    being_delivered=models.BooleanField(default=False,null=True,blank=True)
    received=models.BooleanField(default=False,null=True,blank=True)
    refund_requested=models.BooleanField(default=False,null=True,blank=True)
    refund_granted=models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return str(self.user)

class PasswordReset(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reset_id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    created_when=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"








