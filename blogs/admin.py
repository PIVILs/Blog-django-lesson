from django.contrib import admin

from blogs.models import BlogPost, Entry

admin.site.register(BlogPost)
admin.site.register(Entry)