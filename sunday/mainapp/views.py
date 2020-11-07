from django.shortcuts import render
from django.contrib.auth.forms import  AuthenticationForm


from mainapp.models import Category, Board


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }

    return render(request, 'mainapp/catalog.html', context)


def basket(request):
    return render(request, 'mainapp/basket.html')


def secret(request):
    return render(request, 'mainapp/secret.html')


def catalog_page(request, pk):
    board = Category.objects.filter(category_id=pk)
    context = {
        'boards': board,
        'page_title': 'страница каталога'
    }
    return render(request, 'mainapp/catalog_page.html', context)