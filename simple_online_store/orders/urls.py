from django.urls import include, path
from . import views

urlpatterns = [
	path('basket_adding/', views.basket_adding, name='basket_adding'),
	path('checkout/', views.checkout, name='checkout'),
]