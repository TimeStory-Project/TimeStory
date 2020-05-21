from django.contrib import admin
from common.models import Product
from django.contrib.auth.models import Group

# ModelAdmin Class


class ProductA(admin.ModelAdmin):
    #############################################
    list_display = ('Name', 'availability', 'status')
    #############################################


# Register your models here.
admin.site.register(Product, ProductA)
admin.site.unregister(Group)
