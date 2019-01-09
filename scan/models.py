from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Subscription(models.Model):
    owner = models.CharField(max_length=200)
    qrcode = models.SlugField(max_length=200,
                              unique=True,
                              null=True,
                              blank=True,
                              )

    count_left = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.owner

    @staticmethod
    def get_absolute_url():
        return reverse_lazy('scan:index')


class Visit(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return self.date.strftime('%d.%m.%Y')

