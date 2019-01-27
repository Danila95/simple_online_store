from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	description = models.TextField(blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

# функция, которая выводит нужные значения из поля БД и выводит ее в одну строку в админке
	def __str__(self):
		return "%s %s" % (self.id, self.name)

	# класс который обозначает названия таблиц в единственном и множественном числе в админке
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='products_images/')
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

# функция, которая выводит нужные значения из поля БД и выводит ее в одну строку в админке
	def __str__(self):
		return "%s" % self.id

	# класс который обозначает названия таблиц в единственном и множественном числе в админке
	class Meta:
		verbose_name = 'Фотография'
		verbose_name_plural = 'Фотографии'