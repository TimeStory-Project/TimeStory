from django.db import models

# Create your models here.


class Product(models.Model):
    brand = models.CharField(max_length=50, default="")
    model = models.CharField(max_length=100, default="")
    availability = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="")
    description = models.TextField(default="")
    dial_desp = models.CharField(max_length=100, default="")
    bezel = models.TextField(default="")
    case = models.CharField(max_length=100, default="")
    caseback = models.CharField(max_length=50, default="")
    movement = models.CharField(max_length=100, default="")
    complication = models.TextField(default="")
    strap = models.TextField(default="")
    buckle = models.TextField(default="")
    crystal = models.TextField(default="")
    mainImage = models.ImageField(blank=True, upload_to='images/')

    def Name(self):
        return self.brand + " " + self.model

    def __str__(self):
        return str(self.brand + " " + self.model)


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.product.Name)
