from django.shortcuts import render

from weekapp.models import Week


def week(request):
    weeks = Week.objects.all()
    context = {
        'weeks': weeks,
        'page_title': 'weeks',
    }

    return render(request, 'weekapp/week.html', context)