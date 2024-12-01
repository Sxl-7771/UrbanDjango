from django.views.generic import TemplateView
from django.shortcuts import render


class ClassView(TemplateView):
    template_name = 'second_task/class_view_template.html'


def function_view(request):
    return render(request, 'second_task/function_view_template.html')
