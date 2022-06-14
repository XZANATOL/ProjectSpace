from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_services, name="list_services"),
    path("create", views.create_cart, name="create_cart"),
    path("get_items/<str:cart_name>", views.get_items, name="get_items"),
    path("add_items", views.add_items, name="add_items"),
    path("delete_items", views.delete_items, name="delete_items"),
    path("delete_cart", views.delete_cart, name="delete_cart"),
]
