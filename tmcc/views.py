from django.shortcuts import render
from .models import *
from django import forms
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
import json
# Create your views here.
def index(request):
    return render(request, "tmcc/index.html", {
        "items": Item.objects.all()
    })

def login_view(request):
    if request.method == "GET":
        return render(request, "tmcc/login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else: 
            return render(request, "tmcc/login.html", {"message": "Invalid credentials."})

def register_view(request):
    if request.method == "GET":
        return render(request, "tmcc/register.html")
    elif request.method == "POST":
        print(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")
        try:
            user = User.objects.create_user(email=email, password=password, username=username)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            return render(request, "classroom/register.html", {
                    "message": "Username already taken."
                })


def order_view(request):
    if request.method == "GET":
        try:
            order = Order.objects.get(user=request.user)
        except:
            order = None
        return render(request, "tmcc/order.html", {
            "order": order
        })

def add_to_item(request, id):
    item = Item.objects.get(id=id)
    if request.user.is_authenticated:
        order = Order.objects.get(user=request.user)
        order.item.add(item)
        return JsonResponse({
            "message": "Item successfully added to order."
        })
    else: 
        return HttpResponseRedirect(reverse("index"))

def menu(request):
    return render(request, "tmcc/menu.html", {
        "items": Item.objects.all()
    })
def remove_from_order(request, id):
    if request.user.is_authenticated:
        item = Item.objects.get(id=id)
        order = Order.objects.get(user=request.user)
        try:
            order.item.remove(item)
            message = "Item removed from order."
        except:
            message = "Error: item not in order"
        return JsonResponse({
            "message": message
        })
def social(request):
    return render(request, "tmcc/social.html")
def apply(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = json.loads(request.body)
            username = data["username"]
            work_experience = data["work_experience"]
            email = data["email"]
            newsletter = data["newsletter"]
            questions = data["questions"]
            if newsletter == "true":
                newsletter = True
            else:
                newsletter = False
            try:
                user = User.objects.get(username=username, email=email)
            except:
                return JsonResponse({
                    "message": "Username and email combo does not exist."
                })
            application = Application(work_experince=work_experience, user=user, questions=questions, newsletter=newsletter)
            application.save()
            return JsonResponse({"message": "Success! We will now review you application. Thank you for applying!"})
        elif request.method == "GET":
            return render(request, "tmcc/apply.html")           
    else:
        return HttpResponseRedirect(reverse("index"))
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))