from django.urls import path
from . import views
from .views import watches

urlpatterns = [
    path('', views.home, name='home'),
    path('contactus', views.contactus, name='contactus'),
    path('watches' , views.watches, name='watches'),
    path('<int:pk>/product', views.product, name='product'),

    path('rolexunworn' , views.rolexunworn, name='rolexunworn'),
    path('rolexpreowned', views.rolexpreowned, name='rolexpreowned'),
    path('rolexsold', views.rolexsold, name='rolexsold'),

    path('richardmilleunworn' , views.richardmilleunworn, name='richardmilleunworn'),
    path('richardmillepreowned', views.richardmillepreowned, name='richardmillepreowned'),
    path('richardmillesold', views.richardmillesold, name='richardmillesold'),

    path('patekphilippeunworn' , views.patekphilippeunworn, name='patekphilippeunworn'),
    path('patekphilippepreowned', views.patekphilippepreowned, name='patekphilippepreowned'),
    path('patekphilippesold', views.patekphilippesold, name='patekphilippesold'),

    path('cartierunworn' , views.cartierunworn, name='cartierunworn'),
    path('cartierpreowned', views.cartierpreowned, name='cartierpreowned'),
    path('cartiersold', views.cartiersold, name='cartiersold'),

    path('audemarspiguetunworn' , views.audemarspiguetunworn, name='audemarspiguetunworn'),
    path('audemarspiguetpreowned', views.audemarspiguetpreowned, name='audemarspiguetpreowned'),
    path('audemarspiguetsold', views.audemarspiguetsold, name='audemarspiguetsold')
]