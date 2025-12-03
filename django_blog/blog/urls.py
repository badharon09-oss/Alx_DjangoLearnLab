from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # registration + profile
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # login/logout using Django built-ins
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
]

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]


path('', include('blog.urls')),   # already recommended earlier

from . import views

urlpatterns = [
    # ... existing post urls ...
    # comment creation (POST)
    path('posts/<int:post_pk>/comments/new/', views.comment_create, name='comment-create'),

    # comment edit & delete (by pk)
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]

from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns += [
    path(
        "post/<int:post_id>/comments/new/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),
    path(
        "comment/<int:pk>/edit/",
        CommentUpdateView.as_view(),
        name="comment-edit",
    ),
    path(
        "comment/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment-delete",
    ),
]
