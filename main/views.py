from django.shortcuts import render
from common.models import Product


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def contactus(request):

    return render(request, 'main/contactus.html')

def watches(request):
    #Ignore the redline under Product, it is ok. 
    watches = Product.objects.all()
  

    

    return render(request, 'main/watches.html', {'watches': watches})
