from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# from django.views import View
from django.views.generic import ListView, DetailView, DateDetailView,TemplateView
from django.core.paginator import InvalidPage, Paginator, EmptyPage, PageNotAnInteger
from blog.models import Category, Post, PostImage, Introduction


# Create your views here.
class Home(ListView):
    model = Introduction
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["intro"] = Introduction.objects.filter(status="A")
        if context["intro"]:
            context['message'] = context['intro'][0].html_to_text()

        return context


class SearchView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/search.html"

    def get_queryset(self):
        query = self.request.GET['query']
        title_queryset = Post.objects.filter(status="P", title__icontains=query)
        author_queryset = Post.objects.filter(status="P", author__username__icontains=query)
        date_queryset = Post.objects.filter(status="P", date__icontains=query)
        content_queryset = Post.objects.filter(status="P", content__icontains=query)
        queryset = title_queryset.union(content_queryset).union(author_queryset).union(date_queryset)
        return queryset


class CategoryView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/blog.html"

    queryset = Post.objects.filter(status="P")

    def get_context_data(self):
        context = super().get_context_data()
        category = Category.objects.get(slug=self.request.resolver_match.kwargs.get('slug'))
        context['categories'] = Category.objects.all()
        context['current_category'] = category
        return context

    def get_queryset(self):
        category = Category.objects.get(slug=self.request.resolver_match.kwargs.get('slug'))
        queryset = Post.objects.filter(category=category, status="P")
        return queryset


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/blog.html"
    paginate_by = 6
    queryset = Post.objects.filter(status="P")

    def get_context_data(self):
        context = super().get_context_data()

        context['categories'] = Category.objects.all()
        paginator = Paginator(self.queryset, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
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

