from django.shortcuts import render
from .models import *
from django.forms import forms
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class LoginForm (forms.Form):
    username = ''
def index(request):
    return render(request, "tmcc/index.html", {
        "items": Item.objects.all()
    })

def login_view(request):
    if request.method == "GET":
        return render(request, "tmcc/login.html", {
            "form": LoginForm()
        })
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            login(username, password)
            if login is False:
                return render(request, "tmmc/login.html", {
                    "form": LoginForm(request.POST)
                })
            else: 
                return render(request, "tmcc/index.html")

def register_view(request):
    if request.method == "GET":
        return render(request, "tmmc/register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        


def order_view(request):
    if request.method == "GET":
        return render(request, "tmcc/order.html", {
            "order": request.user.order_items.all()
        })

def add_to_item(request, id):
    item = Item.objects.get(id=id)
    if request.user.is_authenticated:
        if request.method == "POST":
            order = Order.objects.get(user=request.user)
            order.item.add(item)
            return JsonResponse({
                "message": "item successfully added to order."
            })
    else: 
        return HttpResponseRedirect(reverse("index"))

