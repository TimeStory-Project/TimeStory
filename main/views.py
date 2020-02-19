from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def contactus(request):

    return render(request, 'main/contactus.html')

def watches(request):
    return render(request, 'main/watches.html')
