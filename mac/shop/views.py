from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil

# Create your views here.
def index(request):
    products = Products.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil(n/4 - n//4)
    params = {'no_of_slides': nSlides,'range':range(1,nSlides),'products':products}
    return render(request,"shop/index.html",params)
def about(request):
    return render(request,"shop/about.html")
def contact(request):
    return HttpResponse("We are at contact")
def checkout(request):
    return HttpResponse("We are at checkout")
def productview(request):
    return HttpResponse("We are at product view")
def search(request):
    return HttpResponse("We are at search")
def tracker(request):
    return HttpResponse("We are at tracker")