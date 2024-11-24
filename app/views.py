from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def archana(request):
    return HttpResponse('archana is my elder sister')
def swathi(request):
    return HttpResponse('<h1>swathi is my younger sister</h1>')
def archana1(request):
    return HttpResponse('<h1><marquee>archana is my elder sister</marquee></h1>')
def bioData(request):
    return HttpResponse('''<i>my name is sivapriya</i>
                        <b>I am from allur</b>
                        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBOiXJHcvIxPVLBBvb4I0rxXx2vm1SyyPafw&s'>''')
def archana(request):
    return HttpResponse('<i>archana is my elder sister</i>')