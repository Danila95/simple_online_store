from django.shortcuts import render
from .forms import SubscriberForm
# from django.http import HttpResponse

def mainApp(request):
	form = SubscriberForm(request.POST or None)

	return render(request, 'index.html', locals())

# def index(request):
# 	return render(request, 'index.html')
