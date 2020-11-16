from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from basketapp.models import BoardBasket
from mainapp.models import Board




def index(request):
    items = BoardBasket.objects.filter(user=request.user)
    context = {
        'object_list': items,
    }

    return render(request, 'basketapp/basket.html', context)



def add(request, board_id):
    board = Board.objects.get(pk=board_id)
    BoardBasket.objects.get_or_create(
        user=request.user,
        # course_id=course_id
        board=board
    )
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(
        reverse('mainapp:catalog_section',
                kwargs={'category_pk': board.category_id})
    )


def remove(request, board_basket_id):
    item = BoardBasket.objects.get(id=board_basket_id)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))