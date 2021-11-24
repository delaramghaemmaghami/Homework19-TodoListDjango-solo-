from django.urls import path
from .views import *

urlpatterns = [
    path("", welcome_page, name="welcome_page")
]
