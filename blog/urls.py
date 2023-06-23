from . import views
from .views import PostCreateView, PostUpdateView, DeleteView, UserEditView, PasswordsChangeView, ProfilePageView, EditProfilePageView, CreateProfilePageView
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('password/', views.PasswordsChangeView.as_view(template_name='account/change-password.html'), ),
    path('password_success/', views.password_success, name="password_success"),
    path('<int:pk>/profile', views.ProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page', views.CreateProfilePageView.as_view(), name='create_profile_page'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post_update/<int:pk>', views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete'),
]