from django.urls import path
from . import views
from .views import watches

urlpatterns = [
    path('', views.home, name='home'),
    path('contactus', views.contactus, name='contactus'),
    path('watches' , views.watches, name='watches'),
    path('<int:pk>/product', views.product, name='product'),

    path('rolexnew' , views.rolexnew, name='rolexnew'),
    path('rolexused', views.rolexused, name='rolexused')
]