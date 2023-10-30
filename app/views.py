from django.http.response import HttpResponse
from django.http.request import HttpRequest


def hey_view(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")


def how_old_view(request: HttpRequest, end: int, birthyear: int) -> HttpResponse:
    return HttpResponse(end - birthyear)


def take_order_view(
    request: HttpRequest, burgers: int, fries: int, drinks: int
) -> HttpResponse:
    total = (burgers * 4.5) + (fries * 1.5) + drinks
    return HttpResponse(f"${total:,.2f}")
