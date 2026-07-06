from django.contrib import admin
from .models import Category, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)} # Automatically types the slug based on the name

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'category', 'status', 'published_at')
    list_filter = ('status', 'created_at', 'published_at', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('author__username', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_active=True)
