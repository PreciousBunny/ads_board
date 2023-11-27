from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    """
    Класс для работы с моделью Ad (объявлений).
    """
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель')
    image = models.ImageField(upload_to='ads/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        """
        Класс мета-настроек.
        """
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('-created_at',)


class Comment(models.Model):
    """
    Класс для работы с моделью Comment (отзывов).
    """
    text = models.TextField(verbose_name='Отзыв')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.text[:15]}...'

    class Meta:
        """
        Класс мета-настроек.
        """
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-created_at',)
