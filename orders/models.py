from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from goods.models import Good
from django.utils import timezone

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

DELIVERY_TYPE = [
    ('Courier', 'Courier'),
    ('Pickup', 'Pickup')
]

PICKUPS = [
    ('MSU', 'MSU'),
    ('Cosmos_Hotel', 'Cosmos_Hotel'),
    ('Gorod_Mall', 'Gorod_Mall')
]


class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    goods = models.ManyToManyField(OrderGood)
    created_at = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    delivery_options = models.CharField(max_length=150, choices=DELIVERY_TYPE, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    pickup_point = models.CharField(max_length=150, choices=PICKUPS, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(blank=True)

    

    def place_order(self):
        self.created_at = timezone.now()
        self.ordered = True
        self.save()



    def __str__(self):
        return self.user.username + ' ' + str(self.created_at)

    def get_absolute_url(self):
        return reverse('orders:detail', kwargs={'pk':self.pk})


    def get_total(self):
        total = 100
        if self.delivery_options == 'Courier':
            total += 300
        for good in self.goods.all():
            total += good.get_amount()
        return total
