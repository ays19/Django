from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
	return HttpResponse('Welcome to our first Django App')