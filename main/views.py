from django.shortcuts import render
from common.models import Product


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
    individualWatch = Product.objects.get (pk=pk)
    return render(request, 'main/product.html', {'individualWatch':individualWatch})
