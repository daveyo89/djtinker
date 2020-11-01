from blog.models import Category, Post, PostImage, Introduction
from django.contrib import admin


class PostImageAdmin(admin.StackedInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Introduction)
# admin.site.register(Post)
