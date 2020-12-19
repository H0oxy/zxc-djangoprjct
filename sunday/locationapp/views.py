from django.shortcuts import render

from locationapp.models import Location


def location(request):
    locations = Location.objects.all()
    context = {
        'locations': locations,
        'page_title': 'locations',
    }

    return render(request, 'locationapp/location.html', context)