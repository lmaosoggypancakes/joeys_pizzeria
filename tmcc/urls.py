from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="index"),
    path("login", login_view, name="login"),
    path("register", register_view, name="register"),
    path("order", order_view, name="order"),

    # API

    path("api/add/<int:id>", add_to_item, name="add")
]