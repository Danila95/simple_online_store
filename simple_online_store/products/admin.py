from django.contrib import admin
from . models import *

# позволяет вкладывать другие страницы на админке
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0 # убирает дополнительные ряды по загрузке файлов

class ProductAdmin (admin.ModelAdmin):
	# выведем поля в таблице в моделе Subscriber в админке
	list_display = [field.name for field in Product._meta.fields]
	inlines = [ProductImageInline] # вкладываем страницу в ProductAdmin

	class Meta:
		model = Product

# регистрируем модель Product, которую мы импорттировали из models.py и рег. класс ProductAdmin
admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
	# выведем поля в таблице в моделе Subscriber в админке
	list_display = [field.name for field in ProductImage._meta.fields]

	class Meta:
		model = ProductImage


# регистрируем модель Order, которую мы импорттировали из models.py и рег. класс OrderAdmin
admin.site.register(ProductImage, ProductImageAdmin)
