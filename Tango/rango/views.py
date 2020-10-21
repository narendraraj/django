from django.shortcuts import render
from rango.models import Category
from django.http import HttpResponse


# Create your views here.
def homeview(request):
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}

    context_dict['boldletters'] = 'Crunchy, Creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    return render(request, 'rango/home.html', context = context_dict)


def aboutview(request):
    return render(request, 'rango/about.html')


def infoview(request):
    return render(request, 'rango/info.html')
