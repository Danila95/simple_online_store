from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
# from django.http import HttpResponse

def home(request):
	products_images = ProductImage.objects.filter(is_active=True, is_main=True)
	return render(request, 'index.html', locals())


def mainApp(request):
	form = SubscriberForm(request.POST or None)

	if request.method == "POST":
		print(form)
		print(request.POST)
		data = form.cleaned_data

		print(form.cleaned_data)
		print('#####################')
		print(form.cleaned_data['name'])
		print(data['name'])

		# сохранить форму в БД
		new_form = form.save()

	return render(request, 'landing/landing.html', locals())
