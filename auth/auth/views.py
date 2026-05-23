from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request,"index.html")
def handleSignup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if len(username)>10:
            messages.error(request,"Username must be less than 10 characters")
            return redirect("index")
        if pass1 != pass2:
            messages.error(request,"Passwords must match")
            return redirect("index")
        if not(username.isalnum()):
            messages.error(request,"Username must be alphanumeric")
            return redirect("index")

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account is successfully Registered")
        return redirect("index")
    else:
        return HttpResponse("<h1>404 - NOT FOUND</h1>")

# def handleLogin(request):