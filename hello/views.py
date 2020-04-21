from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello This is landing page")

def firstletter(request):
	return HttpResponse("First Letter <a href='/'>Back</a>")

def lastletter(request):
	return HttpResponse("Last letter <a href='firstletter'>back</a>")