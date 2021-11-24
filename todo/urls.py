from django.urls import path
from .views import *

urlpatterns = [
    path("", welcome_page, name="welcome_page"),
    path('', TaskList.as_view(), name="task_list")
]
