from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех блогов
    path('blogs', views.all_blogs, name='blogs'),
    # Страница с подробной информацией по отдельному блогу
    path('blogs/<int:blog_id>/', views.the_blog, name='blog'),
    ]