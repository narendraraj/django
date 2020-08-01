from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_dict ={'boldletters': 'Crunchy, Creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context = context_dict)


