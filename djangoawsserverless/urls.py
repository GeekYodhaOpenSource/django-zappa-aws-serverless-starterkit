from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', views.index, name='main-view')
]