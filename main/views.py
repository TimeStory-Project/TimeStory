from django.shortcuts import render
from common.models import Product
from common.models import ProductImage
from django.db.models import Q

# Create your views here.
def home(request):
    watches = Product.objects.all()
    return render(request, 'main/home.html', {'watches': watches})


def contactus(request):

    return render(request, 'main/contactus.html')

def watches(request):
    #Ignore the redline under Product, it is ok. 
    watches = Product.objects.all()

    return render(request, 'main/watches.html', {'watches': watches})


#This is for the branch create-product-page to test how the inidividual watches will look. 
def product(request,pk):
    individualWatch = Product.objects.get(pk=pk)
    photos = ProductImage.objects.filter(product=individualWatch)
    return render(request, 'main/product.html', {'individualWatch':individualWatch, 'photos':photos})



def rolexnew(request):
    watches = Product.objects.filter(brand="Rolex", condition="Brand new")
    return render(request, 'main/rolexnew.html' , {'watches':watches})



def rolexused(request):
    watches = Product.objects.filter(brand="Rolex").filter(Q(condition="Used but good") | Q(condition="Used but worn"))
    return render(request, 'main/rolexused.html' , {'watches':watches})
