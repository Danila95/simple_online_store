from django.contrib import admin
from . models import *

class SubscriberAdmin (admin.ModelAdmin):
	# выведем поля в таблице в моделе Subscriber в админке
    # list_display = ["name", "email"]
	# Тоже что и выше, только выводится в цикле (выводит все поля, какие есть, даже id)
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name',] # позволяет фильтровать данные по столбцу
    search_fields = ['name', 'email'] # позволяет фильтровать данные с помощью input search

    fields = ["email"] # отображать только поле email в редактировании записи

    # exclude = ["email"] # исключить поле email (исключает возможность редактирования данного поля)
	# inlines = [FieldMappingInline]

	# #list_filter = ('report_data',)
	# search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Subscriber

# регистрируем модель Subscriber, которую мы импорттировали из models.py и рег. класс SubscriberAdmin
admin.site.register(Subscriber, SubscriberAdmin)
