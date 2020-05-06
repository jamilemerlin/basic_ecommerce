from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class ImageModel(models.Model):
    image = models.ImageField(null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False)
    total_in_stock = models.PositiveIntegerField(default=0)
    count_sells = models.PositiveIntegerField(default=0)
    count_views = models.PositiveIntegerField(default=0)
    gallery = models.ManyToManyField(ImageModel, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("products:product_edit", kwargs={"id": self.id})

    def sell(self, amount):
        self.total_in_stock -= amount
        self.count_sells += amount

    def price_integer(self):
        return self.price // 1

    def price_coin(self):
        price = (self.price % 1) * 100
        return price // 1



class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    def total_price(self):
        total = self.amount * self.product.price
        return total




