from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import BoardBasket




def index(request):
    return render(request, 'basketapp/basket.html')


def add(request, board_id):
    # course = Board.objects.get(pk=course_id)
    BoardBasket.objects.get_or_create(
        user=request.user,
        course_id=board_id
    )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponseRedirect(
    #     reverse('mainapp:catalog_section',
    #             kwargs={'category_pk': course.category_id})
    # )