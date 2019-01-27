from django.contrib import admin
from . models import *

# позволяет вкладывать другие страницы на админке
class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0 # убирает дополнительные ряды по загрузке файлов

class OrderAdmin (admin.ModelAdmin):
	# выведем поля в таблице в моделе Subscriber в админке
	list_display = [field.name for field in Order._meta.fields]
	inlines = [ProductInOrderInline]  # вкладываем страницу в OrderAdmin

	class Meta:
		model = Order

# регистрируем модель Order, которую мы импорттировали из models.py и рег. класс OrderAdmin
admin.site.register(Order, OrderAdmin)


class StatusAdmin(admin.ModelAdmin):
	# выведем поля в таблице в моделе Subscriber в админке
	list_display = [field.name for field in Status._meta.fields]

	class Meta:
		model = Status


# регистрируем модель Order, которую мы импорттировали из models.py и рег. класс OrderAdmin
admin.site.register(Status, StatusAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
	# выведем поля в таблице в моделе Subscriber в админке
	list_display = [field.name for field in ProductInOrder._meta.fields]

	class Meta:
		model = ProductInOrder


# регистрируем модель ProductInOrder, которую мы импорттировали из models.py и рег. класс ProductInOrderAdmin
admin.site.register(ProductInOrder, ProductInOrderAdmin)
