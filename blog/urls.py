from . import views
from .views import PostCreateView, PostUpdateView, DeleteView
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post_update/<int:pk>', views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete'),
    path('create_event', views.EventCreateView.as_view(), name='create_event'),
]