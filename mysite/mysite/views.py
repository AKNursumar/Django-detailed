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
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    # print(djtext)
    # print(removepunc)
    analyzed = ""
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[]^_`{|}~'''
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'remove punctuations','analyzed_text':analyzed}
    elif fullcaps == 'on':
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
    elif newlineremover == 'on':
        for char in djtext:
            if char != '/n':
                analyzed += char
        params = {'purpose': 'removed newline', 'analyzed_text': analyzed}
    elif extraspaceremover == 'on':
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed += char
        params = {'purpose': 'removed extra spaced', 'analyzed_text': analyzed}
    elif charcount == 'on':
        count = 0
        for char in djtext:
            count += 1
        analyzed = str(count)
        params = {'purpose': 'Count Characters', 'analyzed_text': analyzed}
    else:
        analyzed = djtext
        params = {'purpose':'to analyze text','analyzed_text':analyzed}
    return render(request,"analyze.html",params)