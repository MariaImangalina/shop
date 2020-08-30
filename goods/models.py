from django.db import models
from django.urls import reverse

class Good(models.Model):
    title = models.CharField(max_length=255)
    weight = models.FloatField(verbose_name='Weight in kg')
    description = models.TextField()
    price = models.FloatField()
    pic = models.ImageField(upload_to='goods/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('goods:detail', kwargs={'pk':self.pk})

