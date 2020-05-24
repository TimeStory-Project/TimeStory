from django.contrib import admin
from common.models import Product, ProductImages
from django.contrib.auth.models import Group

# ModelAdmin Class


class ImageAdmin(admin.TabularInline):
    model = ProductImages
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'availability', 'status')
    inlines = [ImageAdmin]

    class Meta:
        model = Product


@admin.register(ProductImages)
class ProductImageAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    pass


# Register your models here.
admin.site.unregister(Group)
