from django.contrib import admin
from .models import Category, Article, Comment, Reply

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Reply)
