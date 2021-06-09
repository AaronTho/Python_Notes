from django.urls import path
from . import views


# /products ->root
# /products/1/detail -> subfolders

urlpatterns = [
    path('', views.index,),
    path('new', views.new)
]
