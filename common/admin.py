from django.contrib import admin
from common.models import Product, ProductImage
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _

# ModelAdmin Class


class ImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 3
    max_num = 3
    min_num = 3
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            # remove request to avoid "__init__() got an unexpected keyword argument 'request'" error
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" height="100px" /></a>' %
                          (image_url, image_url, file_name))
        output.append(super(AdminFileWidget, self).render(
            name, value, attrs, renderer))
        return mark_safe(u''.join(output))


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_display', 'Name', 'condition', 'updated_at', )
    search_fields = ('brand', 'model', 'model_number', 'condition')
    list_filter = ('brand', 'condition')
    inlines = [ImageAdmin]

    # Show thumbnail in changeview
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'main_image':
            # remove request to avoid "__init__() got an unexpected keyword argument 'request'" error
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ProductAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    class Meta:
        model = Product


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    # Show thumbnail in changeview
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            # remove request to avoid "__init__() got an unexpected keyword argument 'request'" error
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ProductImageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


# Register your models here.
admin.site.unregister(Group)
