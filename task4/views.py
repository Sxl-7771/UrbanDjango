# views.py
from django.shortcuts import render


def shop_view(request):
    games = ["Atomic Heart", "Cyberpunk 2077", "The Witcher 3"]
    return render(request, 'fourth_task/games.html', {'games': games})


def cart_view(request):
    return render(request, 'fourth_task/cart.html')


def home_view(request):
    return render(request, 'fourth_task/platform.html')
