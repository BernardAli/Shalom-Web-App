from django.db import models
from django.urls import reverse

from authy.models import Profile


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class CashFlow(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(default='product.png', upload_to='category_pics')
    receipt_no = models.CharField(max_length=50, blank=True, null=True)
    item_description = models.TextField(blank=True, null=True)
    amount = models.IntegerField(default='0', blank=True, null=True)
    returned_to = models.CharField(max_length=50, blank=True, null=True)
    received_from = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='sale_to')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name


class CashFlowHistory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(default='product.png', upload_to='category_pics')
    receipt_no = models.CharField(max_length=50, blank=True, null=True)
    item_description = models.TextField(blank=True, null=True)
    amount = models.IntegerField(default='0', blank=True, null=True)
    returned_to = models.CharField(max_length=50, blank=True, null=True)
    received_from = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name