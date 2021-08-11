from django.db import models
from django.contrib.auth.models import User
# Класс с товарами

class Categories(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название категории')
    slug = models.SlugField(max_length=20, verbose_name='URL')
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категория'

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')
    description = models.TextField(max_length=150, verbose_name='Описание')
    image = models.ImageField(upload_to='media', verbose_name='Картинка')
    categories_foregin = models.ForeignKey(Categories, on_delete = models.CASCADE, verbose_name='Название категории')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return self.title

# Класс с заказами
class Order(models.Model):
    name = models.CharField(max_length=25, verbose_name='Инициалы')
    email = models.EmailField(max_length=50, verbose_name='E-mail')
    key_product = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name='Название заказа')
    key_product_user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Заказал пользователь')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return self.name
