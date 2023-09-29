from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
# Below that are models

# Banner 
class Banner(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = '1. Banners'
# Category
class Category(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="cat_imgs/")
    
    class Meta:
        verbose_name_plural = '2. Categories'
    def image_tag(self):
        return mark_safe('<img src= "%s" width="50" height = "50" />' % (self.image.url))
    def __str__(self):
        return self.title
# Brand
class Brand(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="brand_imgs/")
    class Meta:
        verbose_name_plural = '3. Brands'
    def __str__(self):
        return self.title
# Color
class Color(models.Model):
    title = models.CharField(max_length = 100)
    color_code = models.CharField(max_length = 100)
    class Meta:
        verbose_name_plural = '4. Colors'
    def color_bg(self):
        return mark_safe('<div style = "width:30px; height:30px; background-color:%s"></div>' % (self.color_code))
    def __str__(self):
        return self.title
# Size
class Size(models.Model):
    title = models.CharField(max_length = 100)
    class Meta:
        verbose_name_plural = '5. Sizes'
    def __str__(self):
        return self.title
# Product model
class Product(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="product_imgs/")
    slug = models.CharField(max_length = 400)
    detail = models.TextField()
    specs = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = '6. Products'
    def __str__(self):
        return self.title

# Product Attribute
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()
    class Meta:
        verbose_name_plural = '7. ProductAttributes'
    def __str__(self):
        return self.product.title

# Add some Data Table of Functionality Purchase
# class lưu trữ thông tin địa chỉ
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state} {self.postal_code}"
# class lưu trữ thông tin đơn hàng (ngày đặt hàng, trạng thái,...)
class Order(models.Model):
    PENDING = 0
    APPROVE = 1
    CANCELED = 2

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (APPROVE, 'Approve'),
        (CANCELED, 'Canceled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"Order {self.id}"
# thông tin giỏ hàng
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
# thông tin sản phẩm
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 

# thông tin thanh toán (ví dụ: số thẻ tín dụng, ngày hết hạn, v.v.)
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    
# thông tin voucher
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField()

