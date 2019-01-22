from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	name = 'Переменная'
	return HttpResponse('<h1>success</h1>')
