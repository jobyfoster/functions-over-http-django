from django.http.response import HttpResponse


def hey_view(request, name):
    return HttpResponse(f"Hey, {name}!")


def how_old_view(request, end, birthyear):
    return HttpResponse(end - birthyear)


def take_order_view(request, burgers, fries, drinks):
    total = (burgers * 4.5) + (fries * 1.5) + drinks
    return HttpResponse(f"${total:,.2f}")
