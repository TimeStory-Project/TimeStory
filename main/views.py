from django.shortcuts import render
from .models import Watch



# Create your views here.
def home(request):
    return render(request, 'home.html')


def contactus(request):

    return render(request, 'contactus.html')

def watches(request):
    context = {
        'watch': Watch
    }
    return render(request, 'watches.html', context)
