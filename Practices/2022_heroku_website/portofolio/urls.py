from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('send_msg/', views.send_msg, name="send_msg"),
]
