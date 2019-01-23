from django.shortcuts import render
from .forms import SubscriberForm
# from django.http import HttpResponse

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

	return render(request, 'index.html', locals())
