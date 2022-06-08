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
    # Страница для добавления нового блога
    path('new_blog/', views.new_blog, name='new_blog'),
    # Страница для добавления новой записи
    path('new_entry/<int:blog_id>/', views.new_entry, name='new_entry')

]