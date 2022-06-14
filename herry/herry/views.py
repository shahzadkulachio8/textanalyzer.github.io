from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalizer = request.POST.get('capitalizer', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    print(removepunc)

    if removepunc == "on":
        punctuations = ''',<.>/?;:"'[]{}\|-)=(*&^%$#@!~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        parmas = {'purpose': 'Removed Punctuations', 'analyed_text': analyzed}
        djtext= analyzed
        # return render(request, 'analyze.html', parmas)


    if capitalizer == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        parmas = {'purpose': ' Capitalized', 'analyed_text': analyzed}
        djtext =analyzed
        # return render(request, 'analyze.html', parmas)


    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.strip(" ")
        parmas = {'purpose': 'Space/New Line Removed', 'analyed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', parmas)


    if charcounter == "on":
        analyzed = len(djtext)
        parmas = {'purpose': 'Total Character Counted', 'analyed_text': analyzed}
        # return render(request, 'analyze.html', parmas)


    if (removepunc!="on" and capitalizer!="on" and newlineremover!="on" and charcounter!="on"):
        return HttpResponse("<h1> Error </h1>")

    return render(request, 'analyze.html', parmas)
