
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('upload', views.upload),
    path('success', views.success),
]
