from django.contrib import admin
from . models import *

# позволяет вкладывать страницы в другие страницы на админке
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0 # убирает дополнительные ряды по загрузке файлов

class ProductAdmin (admin.ModelAdmin):
	# выведем поля таблицы из моделе Product в админке
	list_display = [field.name for field in Product._meta.fields]
	inlines = [ProductImageInline] # вкладываем страницу в ProductAdmin

	class Meta:
		model = Product

# регистрируем модель Product, которую мы импортировали из models.py и рег. класс ProductAdmin
admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
	# выведем поля таблицы из моделе ProductImage в админке
	list_display = [field.name for field in ProductImage._meta.fields]

	class Meta:
		model = ProductImage


# регистрируем модель ProductImage, которую мы импортировали из models.py и рег. класс ProductImageAdmin
admin.site.register(ProductImage, ProductImageAdmin)


class СurrencyAdmin(admin.ModelAdmin):
	# выведем поля таблицы из моделе Сurrency в админке
	list_display = [field.name for field in Сurrency._meta.fields]

	class Meta:
		model = Сurrency


# регистрируем модель Сurrency, которую мы импортировали из models.py и рег. класс СurrencyAdmin
admin.site.register(Сurrency, СurrencyAdmin)



class ProductCategoryAdmin(admin.ModelAdmin):
	# выведем поля таблицы из моделе Сurrency в админке
	list_display = [field.name for field in ProductCategory._meta.fields]

	class Meta:
		model = ProductCategory


# регистрируем модель ProductCategory, которую мы импортировали из models.py и рег. класс ProductCategoryAdmin
admin.site.register(ProductCategory, ProductCategoryAdmin)