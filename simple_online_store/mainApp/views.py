from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
# from django.http import HttpResponse

def home(request):
	products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
	products_images_phones = products_images.filter(product__category__id=1)
	products_images_laptops = products_images.filter(product__category__id=2)
	products_images_headphones = products_images.filter(product__category__id=3)
	products_images_different = products_images.filter(product__category__id=4)
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
