from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from website.settings import AUTH_USER_MODEL


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to="picture")
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail_product", kwargs={"slug": self.slug})


class Customer(AbstractUser):
    name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.PositiveIntegerField()
    password = models.PositiveIntegerField()
    password_confirm = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.product.name} [{self.quantity}]"


class Cart(models.Model):
    customer = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered_cart = models.BooleanField(default=False)
    ordered_date_cart = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return self.customer.name