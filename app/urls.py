from django.urls import path
from app.views import *

urlpatterns = [
    path("", index, name="home"),
    path("photo/<str:numb>", photo, name="photo"),
]