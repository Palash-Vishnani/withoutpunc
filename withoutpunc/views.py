from django.http import HttpResponse
from django.shortcuts import render
from django.urls.resolvers import CheckURLMixin

def index(request):
    return render(request,'index.html')

def analysed(request):
    text=request.POST.get('text','default')
    check1=request.POST.get('check1','off')
    check2=request.POST.get('check2','off')
    check3=request.POST.get('check3','off')
    check4=request.POST.get('check4','off')
    analyse=""
    if check1=="on":
        analyse=""
        punc=""".?!:;-()[]...’“”/,"""
        for char in text:
            if char not in punc:
                analyse=analyse+char
        text=analyse

    if check3=="on":
        analyse=""
        for char in text:
            analyse = analyse + char.upper()
        text=analyse

    if check4=="on":
        analyse=""
        for char in text:
            if char != "\n" and char !="\r":                                                                                        
                analyse = analyse + char
        text=analyse
    params={"output":analyse}

    if check2=="on":
        i=0
        for char in text:
            if char not in [" ","\n"]:
                i=i+1
        analyse=text
        params={"output":analyse,"total":"Total number of characters:","total_char":i}
        return render(request,'analysed.html',params)

    if check1=="off" and check2=="off" and check3== "off" and check4=="off":
        return HttpResponse("Unable to modify the string")
        
    return render(request,'analysed.html',params)