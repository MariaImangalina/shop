from django.db import models
from django.urls import reverse

class Good(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(verbose_name='Price in RUR')
    pic = models.ImageField(upload_to='goods/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('goods:detail', kwargs={'pk':self.pk})
