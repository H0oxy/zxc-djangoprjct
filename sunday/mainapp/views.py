from django.shortcuts import render

from mainapp.models import Category


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

