from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def home_page(request):
    return render(request, "home_page.html")


def function_view(request):
    return render(request, "func_template.html")


class ClassView(TemplateView):
    template_name = "class_template.html"
