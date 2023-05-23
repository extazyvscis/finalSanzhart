from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('post/add/', views.add_post, name='add_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
