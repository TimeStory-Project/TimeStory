from django.db import models

# Create your models here.

BRAND_CHOICES = (
    ('Rolex','Rolex'),
    ('Audemars Piguet', 'Audemars Piguet'),
    ('Patek Philippe','Patek Philippe'),
    ('Richard Mille','Richard Mille'),
    ('Cartier','Cartier'),
)

CONDITION_CHOICES = (
    ('Brand new', 'Brand new'),
    ('Used but good', 'Used but good'),
    ('Used but worn', 'Used but worn'),
    ('Sold', 'Sold'),
)


class Product(models.Model):
    brand = models.CharField(max_length=50, default="", choices=BRAND_CHOICES)
    model = models.CharField(max_length=100, default="")
    model_number = models.CharField(max_length=100, default="")
    availability = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    condition = models.CharField(max_length=20, default="", choices=CONDITION_CHOICES)
    description = models.TextField(default="")
    dial_desp = models.CharField(max_length=100, default="", blank=True)
    bezel = models.TextField(default="", blank=True)
    case = models.CharField(max_length=100, default="", blank=True)
    caseback = models.CharField(max_length=50, default="", blank=True)
    movement = models.CharField(max_length=100, default="", blank=True)
    complication = models.TextField(default="", blank=True)
    strap = models.TextField(default="", blank=True)
    buckle = models.TextField(default="", blank=True)
    crystal = models.TextField(default="", blank=True)
    mainImage = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
