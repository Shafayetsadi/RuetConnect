from django.urls import path
from django.conf.urls import include
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='campus-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/upvote', views.upvote, name='upvote'),
    path('post/<int:pk>/downvote', views.downvote, name='downvote'),
    path('post/<int:pk>/add_comment/', CommentCreateView.as_view(), name='add-comment'),
    path('about/', views.about, name='campus-about'),
    path('r/<str:thread_name>/', views.thread, name='campus-thread'),

    path('search/', views.search, name='search'),

    path('markdownx/', include('markdownx.urls')),
]
