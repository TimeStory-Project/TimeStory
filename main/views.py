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
        return render(request, 'main/contactUs.html', {'page':page})

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
        
        elif 'pricehightolow' in request.GET:
            watches = Product.objects.all()
            watches = watches.order_by('-price')
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
        return render(request, "main/watches.html" , {'queries': queries, 'page':page})

    else: 
        individualWatch = Product.objects.get(pk=pk)
        photos = ProductImage.objects.filter(product=individualWatch)
        return render(request, 'main/product.html', {'individualWatch':individualWatch, 'photos':photos, 'page':page})



def rolexunworn(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Rolex", condition="Unworn")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/rolexunworn.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/rolexunworn.html', {'watches': watches, 'page':page})
    else: 
        return render(request, 'main/rolexunworn.html' , {'watches':watches, 'page':page})

def rolexpreowned(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Rolex", condition="Preowned")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/rolexpreowned.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/rolexpreowned.html', {'watches': watches, 'page':page})

    else:
        return render(request, 'main/rolexpreowned.html' , {'watches':watches, 'page':page})

def rolexsold(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Rolex", condition="Sold")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/rolexsold.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/rolexsold.html', {'watches': watches, 'page':page})

    else:
        return render(request, 'main/rolexsold.html' , {'watches':watches, 'page':page})



def richardmilleunworn(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Richard Mille", condition="Unworn")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/richardmilleunworn.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/richardmilleunworn.html', {'watches': watches, 'page':page})
    else: 
        return render(request, 'main/richardmilleunworn.html' , {'watches':watches, 'page':page})

def richardmillepreowned(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Richard Mille", condition="Preowned")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/richardmillepreowned.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/richardmillepreowned.html', {'watches': watches, 'page':page})
    else:         
        return render(request, 'main/richardmillepreowned.html' , {'watches':watches, 'page':page})

def richardmillesold(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Richard Mille", condition="Sold")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/richardmillesold.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/richardmillesold.html', {'watches': watches, 'page':page})
    else:        
        return render(request, 'main/richardmillesold.html' , {'watches':watches, 'page':page})





def patekphilippeunworn(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Patek Philippe", condition="Unworn")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/patekphilippeunworn.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/patekphilippeunworn.html', {'watches': watches, 'page':page})
    else: 
        return render(request, 'main/patekphilippeunworn.html' , {'watches':watches, 'page':page})

def patekphilippepreowned(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Patek Philippe", condition="Preowned")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/patekphilippepreowned.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/patekphilippepreowned.html', {'watches': watches, 'page':page})
    else: 
        return render(request, 'main/patekphilippepreowned.html' , {'watches':watches, 'page':page})

def patekphilippesold(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Patek Philippe", condition="Sold")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/patekphilippesold.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/patekphilippesold.html', {'watches': watches, 'page':page})
    else: 

        return render(request, 'main/patekphilippesold.html' , {'watches':watches, 'page':page})




def cartierunworn(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Cartier", condition="Unworn")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/cartierunworn.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/cartierunworn.html', {'watches': watches, 'page':page})
    else: 
        return render(request, 'main/cartierunworn.html' , {'watches':watches, 'page':page})

def cartierpreowned(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Cartier", condition="Preowned")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/cartierpreowned.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/cartierpreowned.html', {'watches': watches, 'page':page})
    else:       
        return render(request, 'main/cartierpreowned.html' , {'watches':watches, 'page':page})

def cartiersold(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Cartier", condition="Sold")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/cartiersold.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/cartiersold.html', {'watches': watches, 'page':page})
    else:       

        return render(request, 'main/cartiersold.html' , {'watches':watches, 'page':page})



def audemarspiguetunworn(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Audemars Piguet", condition="Unworn")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/audemarspiguetunworn.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/audemarspiguetunworn.html', {'watches': watches, 'page':page})
    else:       

        return render(request, 'main/audemarspiguetunworn.html' , {'watches':watches, 'page':page})

def audemarspiguetpreowned(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Audemars Piguet", condition="Preowned")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/audemarspiguetpreowned.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/audemarspiguetpreowned.html', {'watches': watches, 'page':page})
    else:   
        return render(request, 'main/audemarspiguetpreowned.html' , {'watches':watches, 'page':page})

def audemarspiguetsold(request):
    page = 'watches'
    watches = Product.objects.filter(brand="Audemars Piguet", condition="Sold")

    if request.GET:
        if 'price' in request.GET:
            watches = watches.order_by('price')
            return render(request, 'main/audemarspiguetsold.html', {'watches': watches, 'page':page})
            
        elif 'pricehightolow' in request.GET:
            watches = watches.order_by('-price')
            return render(request, 'main/audemarspiguetsold.html', {'watches': watches, 'page':page})
    else:   
        return render(request, 'main/audemarspiguetsold.html' , {'watches':watches, 'page':page})    



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


