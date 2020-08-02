from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homeview(request):
    context_dict ={'boldletters': 'Crunchy, Creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/home.html', context = context_dict)


def aboutview(request):
    return render(request, 'rango/about.html')

def infoview(request):
    return render(request, 'rango/info.html')