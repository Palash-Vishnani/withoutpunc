from django.http import HttpResponse
from django.shortcuts import render
from django.urls.resolvers import CheckURLMixin

def index(request):
    return render(request,'index.html')

def analyzed(request):
    text=request.POST.get('text','default')
    check1=request.POST.get('check1','off')
    check2=request.POST.get('check2','off')
    check3=request.POST.get('check3','off')
    check4=request.POST.get('check4','off')
    analyze=""
    if check1=="on":
        analyze=""
        punc=""".?!:;-()[]...’“”/,"""
        for char in text:
            if char not in punc:
                analyze=analyze+char
        text=analyze

    if check3=="on":
        analyze=""
        for char in text:
            analyze = analyze + char.upper()
        text=analyze

    if check4=="on":
        analyze=""
        for char in text:
            if char != "\n" and char !="\r":                                                                                        
                analyze = analyze + char
        text=analyze
    params={"output":analyze}

    if check2=="on":
        i=0
        for char in text:
            if char not in [" ","\n"]:
                i=i+1
        analyze=text
        params={"output":analyze,"total":"Total number of characters:","total_char":i}
        return render(request,'analyzed.html',params)

    if check1=="off" and check2=="off" and check3== "off" and check4=="off":
        return HttpResponse("Unable to modify the string")
        
    return render(request,'analyzed.html',params)