from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Category, Post, PostImage


# Create your views here.
class SearchView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/search.html"

    def get_queryset(self):
        query = self.request.GET['query']
        title_queryset = Post.objects.filter(status="P", title__icontains=query)
        content_queryset = Post.objects.filter(status="P", content__icontains=query)
        queryset = title_queryset.union(content_queryset)
        return queryset


class CategoryView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/category.html"
    queryset = Post.objects.filter(status="P")

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        category = Category.objects.get(slug=self.request.resolver_match.kwargs.get('slug'))
        queryset = Post.objects.filter(category=category, status="P")
        return queryset


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/index.html"
    queryset = Post.objects.filter(status="P")

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    queryset = Post.objects.filter(status="P")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        post = self.get_object()
        context['categories'] = Category.objects.all()
        context['photos'] = PostImage.objects.filter(post=post)
        return context


class PhotoDetailView(DetailView):
    model = PostImage
    context_object_name = "photo"
    template_name = "blog/photo_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        photo = self.get_object()

        context["photo"] = photo
        return context

