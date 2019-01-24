from django.db import models

class Subscriber(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=128)

# функция, которая выводит нужные значения из поля БД и выводит ее в одну строку в админке
	def __str__(self):
			return 'id: %s Пользователь: %s email: %s' % (self.id, self.name, self.email)


	# def __str__(self):
	# 	try:
	# 		return self.user.username
	# 	except:
	# 		return '%s' % self.user.id

	# класс который обозначает названия таблиц в единственном и множественном числе в админке
	class Meta:
		verbose_name = 'MySubscriber'
		verbose_name_plural = 'A lot of Subscribers'