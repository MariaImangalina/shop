from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from goods.models import Good

User = get_user_model()

class OrderGood(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, related_name='order_good', on_delete=models.CASCADE)

    def __str__(self):
        return self.good.title

    def get_amount(self):
        return self.quantity * self.good.price


class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    goods = models.ManyToManyField(OrderGood)
    created_at = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('orders:detail', kwargs={'pk':self.pk})

    def get_total(self):
        total = 0
        for good in self.goods.all():
            total += good.get_amount
        return total
