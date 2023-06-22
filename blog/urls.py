from . import views
from .views import PostCreateView, PostUpdateView, DeleteView, UserEditView, PasswordsChangeView
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('password/', views.PasswordsChangeView.as_view(template_name='account/change-password.html'), ),
    path('password_success/', views.password_success, name="password_success"),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post_update/<int:pk>', views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete'),
]