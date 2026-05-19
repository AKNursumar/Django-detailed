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
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(removepunc == "off" and fullcaps == "off" and extraspaceremover == "off" and newlineremover == "off"):
        return HttpResponse(djtext + "</br>Nothing Changed")
    return render(request, 'analyze.html', params)