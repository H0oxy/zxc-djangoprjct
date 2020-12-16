from django.shortcuts import render

from sponsorapp.models import Sponsor


def sponsor(request):
    sponsors = Sponsor.objects.all()
    context = {
        'sponsors': sponsors,
        'page_title': 'спонсоры',
    }

    return render(request, 'sponsorapp/sponsor.html', context)