from django.urls import include, path, re_path
from products import views

urlpatterns = [
	# path('', views.mainApp, name='index'),
	path(r'product/<int:product_id>', views.product, name='product'),
]