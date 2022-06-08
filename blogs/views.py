from django.shortcuts import render, redirect
from .models import BlogPost, Entry
from .forms import BlogForm, EntryForm

def index(request):
    """Домашняя страница приложения Blog"""
    return render(request, 'blogs/index.html')

def all_blogs(request):
    """Выводит срисок всех блогов."""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def the_blog(request, blog_id):
    """Выводит один блог и все его записи."""
    blog = BlogPost.objects.get(id=blog_id)
    entries = blog.entry_set.order_by('date_added')
    context = {'blog': blog, 'entries': entries}
    return render(request, 'blogs/blog.html', context)

def new_blog(request):
    """Определяет новый блог."""
    if request.method != 'POST':
        # Данные не отправлялись, создается пустая форма.
        form = BlogForm()
    else:
        # Отправлены данные POST, обработать данные.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')

    # Вывести пустую или не действующую форму.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def new_entry(request, blog_id):
    """ Добавляет новую запись в конкретном блоге."""
    blog = BlogPost.objects.get(id=blog_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blog = blog
            new_entry.save()
            return redirect('blogs:blog', blog_id=blog_id)

    context = {'blog':blog, 'form': form}
    return render(request, 'blogs/new_entry.html', context)

def edit_entry(request, entry_id):
    """ Редактирует существующую запись."""
    entry = Entry.objects.get(id=entry_id)
    blog = entry.blog

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'entry': entry, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_entry.html', context)