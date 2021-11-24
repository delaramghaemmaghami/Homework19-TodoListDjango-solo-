from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import *


def welcome_page(request):
    return render(request, "welcomepage.html")


class TaskList(ListView):
    model = Task
    template_name = "todo/todo_detail.html"
