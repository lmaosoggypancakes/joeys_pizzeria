from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path("", index, name="index"),
    path("login", login_view, name="login"),
    path("register", register_view, name="register"),
    path("menu", menu, name="menu"),
    path("order", order_view, name="order"),
    path('social', views.social, name='social'),
    path('apply', views.apply, name='apply'),
    path('logout', views.logout_view, name='logout'),

    # API

    path("api/add/<int:id>", add_to_item, name="add"),
    path("api/remove/<int:id>", remove_from_order, name="remove"),
]