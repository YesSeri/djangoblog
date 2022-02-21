from django.contrib import admin

# Register your models here.

from .models import Post, Topic


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'id')
    fields = ('title', 'content', 'author', 'topic', 'created_date')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
