from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False)
    total_in_stock = models.PositiveIntegerField(default=0)
    count_sells = models.PositiveIntegerField(default=0)
    count_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #    return f"/products/{self.id}/"
    # def para criar url no title do produto.

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("products:product_edit", kwargs={"id": self.id})

    def sell(self, amount):
        self.total_in_stock -= amount
        self.count_sells += amount
