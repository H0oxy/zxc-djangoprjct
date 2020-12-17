from django.shortcuts import render

from computerapp.models import Computer


def computer(request):
    computers = Computer.objects.all()
    context = {
        'computers': computers,
        'page_title': 'computers',
    }

    return render(request, 'computerapp/computer.html', context)