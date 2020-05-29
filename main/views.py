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

def rolexsold(request):
    watches = Product.objects.filter(brand="Rolex", condition="Sold")
    return render(request, 'main/rolexnew.html' , {'watches':watches})



def richardmillenew(request):
    watches = Product.objects.filter(brand="Richard Mille", condition="Brand new")
 
    return render(request, 'main/richardmillenew.html' , {'watches':watches})

def richardmilleused(request):
    watches = Product.objects.filter(brand="Richard Mille").filter(Q(condition="Used but good") | Q(condition="Used but worn"))
    return render(request, 'main/richardmilleused.html' , {'watches':watches})

def richardmillesold(request):
    watches = Product.objects.filter(brand="Richard Mille", condition="Sold")
    return render(request, 'main/richardmillenew.html' , {'watches':watches})





def patekphilippenew(request):
    watches = Product.objects.filter(brand="Patek Philippe", condition="Brand new")
 
    return render(request, 'main/patekphilippenew.html' , {'watches':watches})

def patekphilippeused(request):
    watches = Product.objects.filter(brand="Patek Philippe").filter(Q(condition="Used but good") | Q(condition="Used but worn"))
    return render(request, 'main/patekphilippeused.html' , {'watches':watches})

def patekphilippesold(request):
    watches = Product.objects.filter(brand="Patek Philippe", condition="Sold")
    return render(request, 'main/patekphilippenew.html' , {'watches':watches})




def cartiernew(request):
    watches = Product.objects.filter(brand="Cartier", condition="Brand new")
 
    return render(request, 'main/cartiernew.html' , {'watches':watches})

def cartierused(request):
    watches = Product.objects.filter(brand="Cartier").filter(Q(condition="Used but good") | Q(condition="Used but worn"))
    return render(request, 'main/cartierused.html' , {'watches':watches})

def cartiersold(request):
    watches = Product.objects.filter(brand="Cartier", condition="Sold")
    return render(request, 'main/cartiernew.html' , {'watches':watches})



