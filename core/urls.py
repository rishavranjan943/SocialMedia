from django.urls import path
from .views import *

urlpatterns=[
    path('',feed, name='feed'),
    path('my_post/', index, name='index'),
    path('create/',create_post,name='create_post'),
    path('post/like/', liked_by, name='liked_by'),
]