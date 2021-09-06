from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "home.html", {
        "success_message": "Your successfully Logged In"
    })
    
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse(home))
        else:
            return render(request, "login.html", {
                "error_message": "Invalid Credentials!"
            })
    return render(request, "login.html")
    

def logout(request):
    auth_logout(request)
    return render(request, "login.html", {
        "success_message": "Your successfully Logged Out"
    })