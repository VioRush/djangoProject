from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),   # zostaje wyświetlone w ../blog co jest napisane we views.py pod def index
    path('posts', views.post_list, name='post_list'),
    path('posts/<int:post_id>', views.post_detail, name='post_detail'),
]
