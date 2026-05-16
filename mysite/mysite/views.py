from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # identity = {'name':'AK','place':'Gondal'}
    # # return HttpResponse('''<a href = "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django playlist </a>''')
    # return render(request, "index.html",identity)
    return render(request,"index.html")
def about(request):
    return HttpResponse("About")
def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse("Remove punctuation")
def Capfirst(request):
    return HttpResponse("Capitalize")
def newlineremove(request):
    return HttpResponse('new line remove <a href = "/">return to home page</a>')
def spaceremove(request):
    return HttpResponse("Space remove")
def Charcount(request):
    return HttpResponse("Char count")
def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(djtext)
    print(removepunc)
    return render(request,"index.html")