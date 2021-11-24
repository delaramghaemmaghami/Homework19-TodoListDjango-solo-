from django.urls import path
from .views import *

urlpatterns = [
    path("", welcome_page, name="welcome_page"),
    path("taskList", TaskList.as_view(), name="task_list")
]
