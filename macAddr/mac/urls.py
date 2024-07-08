"""import the view function"""
from django.urls import path
from . import views
urlpatterns = [
    path("ping/",views.ping),
]
