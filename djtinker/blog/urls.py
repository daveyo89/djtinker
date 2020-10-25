from django.urls import path

from blog.views import SearchView, CategoryView, PostListView, PostDetailView, PhotoDetailView

urlpatterns = [
    path('search', SearchView.as_view(), name="search"),
    path('category/<slug:slug>', CategoryView.as_view(), name="category"),

    path('', PostListView.as_view(), name="index"),
    path('posts/<slug:slug>', PostDetailView.as_view(), name="post-detail"),
    path('photos/<int:pk>', PhotoDetailView.as_view(), name="photo-detail"),
]
