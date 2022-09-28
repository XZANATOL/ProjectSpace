from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.blog_home, name="blog_home"),
    path("send_msg/", views.send_msg, name="feedback_sender"),
    path('<str:cat>/', views.posts_in_cat, name="posts_in_cat"),
    path('<str:cat>/<str:slug>/', views.post_in_detail, name="post_in_detail")
]
