from blog.models import Category, Post, PostImage
from django.contrib import admin


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Category)
# admin.site.register(Post)
