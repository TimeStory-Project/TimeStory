from django.shortcuts import render
from common.models import Product
from common.models import ProductImage, Banner
from django.db.models import Q


# Create your views here.
def home(request):
    #For search-bar trying to implement
    query = ""
    page = 'home'
    if request.GET:
        query = request.GET['q']
        queries = get_blog_queryset(query)
        return render(request, "main/watches.html" , {'queries': queries, 'page':'watches'})

    else:
        watches = Product.objects.all()
        banner = Banner.objects.all()
        return render(request, 'main/home.html', {'watches': watches, 'banner': banner, 'page':page})


def contactus(request):
    #For search-bar trying to implement
    query = ""
    page = 'contactus'
    if request.GET:
        query = request.GET['q']
        queries = get_blog_queryset(query)
        return render(request, "main/watches.html" , {'queries': queries, 'page':'watches'})

    else:
        return render(request, 'main/contactus.html', {'page':page})

def watches(request):
    #For search-bar trying to implement
    page = 'watches'
    if request.GET:
        if 'q' in request.GET: #this is for the search
            query = request.GET['q']
            queries = get_blog_queryset(query)
            return render(request, "main/watches.html" , {'queries': queries, 'page':page})

        elif 'price' in request.GET:
            watches = Product.objects.all()
            watches = watches.order_by('price')
            return render(request, 'main/watches.html', {'watches': watches, 'page':page})
    
        elif 'new' in request.GET:
            watches = Product.objects.all()
            watches = watches.order_by('-created_at')
            return render(request, 'main/watches.html', {'watches': watches, 'page':page})

        else:
            watches = Product.objects.all()
            return render(request, 'main/watches.html', {'watches': watches, 'page':page})

    else:
        watches = Product.objects.all()
        return render(request, 'main/watches.html', {'watches': watches, 'page':page})


#This is for the branch create-product-page to test how the inidividual watches will look. 
def product(request,pk):
    request.session['order'] = 'asc'
    #For search-bar trying to implement
    query = ""
    page = 'watches'
    if request.GET:
        query = request.GET['q']
        queries = get_blog_queryset(query)
        return render(request, "main/watches.html" , {'queries': queries})

    else: 
        individualWatch = Product.objects.get(pk=pk)
        photos = ProductImage.objects.filter(product=individualWatch)
        return render(request, 'main/product.html', {'individualWatch':individualWatch, 'photos':photos, 'page':page})



def rolexnew(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Rolex", condition="Brand new")
    return render(request, 'main/rolexnew.html' , {'watches':watches, 'page':page})

def rolexused(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Rolex").filter(Q(condition="Used but good") | Q(condition="Used but worn"))
    return render(request, 'main/rolexused.html' , {'watches':watches, 'page':page})

def rolexsold(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Rolex", condition="Sold")
    return render(request, 'main/rolexnew.html' , {'watches':watches, 'page':page})



def richardmillenew(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Richard Mille", condition="Brand new")
    return render(request, 'main/richardmillenew.html' , {'watches':watches, 'page':page})

def richardmilleused(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Richard Mille").filter(Q(condition="Used but good") | Q(condition="Used but worn"))
    return render(request, 'main/richardmilleused.html' , {'watches':watches, 'page':page})

def richardmillesold(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Richard Mille", condition="Sold")
    return render(request, 'main/richardmillenew.html' , {'watches':watches, 'page':page})





def patekphilippenew(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Patek Philippe", condition="Brand new")
    return render(request, 'main/patekphilippenew.html' , {'watches':watches, 'page':page})

def patekphilippeused(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Patek Philippe").filter(Q(condition="Used but good") | Q(condition="Used but worn"))
    return render(request, 'main/patekphilippeused.html' , {'watches':watches, 'page':page})

def patekphilippesold(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Patek Philippe", condition="Sold")
    return render(request, 'main/patekphilippenew.html' , {'watches':watches, 'page':page})




def cartiernew(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Cartier", condition="Brand new")
    return render(request, 'main/cartiernew.html' , {'watches':watches, 'page':page})

def cartierused(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Cartier").filter(Q(condition="Used but good") | Q(condition="Used but worn"))
    return render(request, 'main/cartierused.html' , {'watches':watches, 'page':page})

def cartiersold(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Cartier", condition="Sold")
    return render(request, 'main/cartiernew.html' , {'watches':watches, 'page':page})



def audemarspiguetnew(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Audemars Piguet", condition="Brand new")
    return render(request, 'main/audemarspiguetnew.html' , {'watches':watches, 'page':page})

def audemarspiguetused(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Audemars Piguet").filter(Q(condition="Used but good") | Q(condition="Used but worn"))
    return render(request, 'main/audemarspiguetused.html' , {'watches':watches, 'page':page})

def audemarspiguetsold(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Audemars Piguet", condition="Sold")
    return render(request, 'main/audemarspiguetnew.html' , {'watches':watches, 'page':page})    



def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ") #Eg input rolex mariner, it will split into a list containing [rolex,mariner]
    for q in queries:
        posts = Product.objects.filter(
                Q(brand__icontains=q) |
                Q(model__icontains=q) |
                Q(description__icontains=q) |
                Q(model_number__icontains=q)
            ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))


