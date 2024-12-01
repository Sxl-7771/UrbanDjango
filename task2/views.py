# task2/views.py
from django.shortcuts import render
from django.views import View


class ClassBasedView(View):
    def get(self, request):
        return render(request, '../templates/second_task/class_based.html', {'message': 'Это шаблон для классового представления'})


def function_based_view(request):
    return render(request, '../templates/second_task/function_based.html', {'message': 'Это шаблон для функционального представления'})
