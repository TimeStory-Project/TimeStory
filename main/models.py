from django.db import models

# Create your models here.


class Watch(models.Model):
    model = models.CharField(max_length=100)
    availability = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=20)
    dial_desp = models.CharField(max_length=50)
    bezel = models.CharField(max_length=100)
    case = models.CharField(max_length=100)
    caseback = models.CharField(max_length=100)
    movement = models.CharField(max_length=100)
    complication = models.CharField(max_length=500)
    strap = models.CharField(max_length=100)
    buckle = models.CharField(max_length=100)
    crystal = models.CharField(max_length=100)


