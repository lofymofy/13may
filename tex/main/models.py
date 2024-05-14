
# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)  # Максимальная длина +7-xxx-xx-xx-xx

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Tovar(models.Model):

    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


    def __str__(self):
        return self.name


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)

    problem = models.CharField(max_length=250)
    amount = models.IntegerField()
    is_send = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.user.username} {self.tovar.name}'