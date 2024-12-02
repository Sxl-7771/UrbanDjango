from django.shortcuts import render


def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    items = {
        'item1': 'Пункт 1',
        'item2': 'Пункт 2',
        'item3': 'Пункт 3',
    }
    return render(request, 'third_task/shop.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')
