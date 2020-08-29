from django.db import models

class Good(models.Model):
    title = models.CharField(max_length=255)
    weight = models.FloatField(verbose_name='Weight in kg')
    description = models.TextField()
    price = models.FloatField()
    pic = models.ImageField(upload_to='goods/')

    def __str__(self):
        return self.title

