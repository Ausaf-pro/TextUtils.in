# This view file is made by Ausaf Hussain on 21-08-2020(Friday) :

# Impoting django.http and HttpResponse files..

from django.http import HttpResponse
from django.shortcuts import render

# Function for the Home page of out Website
def index(request):
    return render(request, 'index2.html')


# Function for the Page that the Home page will redirect i.e. to the analyze2.html
def analyze(request):
    # Get the text
    global mayhem
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('removespace', 'off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        mayhem = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', mayhem)



    if fullcaps == "on":
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        mayhem = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', mayhem)


    if newlineremove == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        mayhem = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', mayhem)

    if (extraspaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        mayhem = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', mayhem)

    if (removepunc != "on" and newlineremove != "on" and extraspaceremove != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyzed2.html', mayhem)

    else:
        return HttpResponse('You cannot access this Webpage. This page is under construction..')

