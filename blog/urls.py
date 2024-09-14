from django.urls import path

from .views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="blog/post_new"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="blog/post_edit"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="blog/post_detail"),
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog/post_delete"),
]
