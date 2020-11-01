from django.shortcuts import render
from rango.models import Category
from rango.models import Page

# Create your views here.


def homeview(request):
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}

    context_dict['boldletters'] = 'Crunchy, Creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    return render(request, 'rango/home.html', context=context_dict)


def aboutview(request):
    return render(request, 'rango/about.html')


def infoview(request):
    return render(request, 'rango/info.html')


def show_category(request, category_name_slug):
    # Create a context dictionay we can pass
    # to the tmplate rendering engine.

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)
