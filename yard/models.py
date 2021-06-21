from django.db import models
from django.utils.safestring import mark_safe
import os

class Sphere(models.Model):
    name = models.CharField('Вид деятельности', max_length=20)
    prefix = models.CharField('Префикс', max_length=3, blank=True,)

    def dot_prefix(self):
        return str('.' + str(self.prefix))

    class Meta:
        verbose_name = '   Вид деятельности'
        verbose_name_plural = '   Виды деятельности'

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.ForeignKey(Sphere, on_delete=models.CASCADE)
    short_description = models.CharField('Краткое описание', max_length=120, blank=True,)
    long_description = models.CharField('Полное описание', max_length=900, blank=True,)
    slogan = models.CharField('Слоган после заголовка', max_length=30, blank=True,)
    image = models.FileField('Фото', blank=True)
    service_id = models.CharField('service id в шаблоне', max_length=30, blank=True,)

    def anchor(self):
        return str('#' + str(self.service_id))

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = '  Подробно о виде деятельности'
        verbose_name_plural = '  Подробно о видах деятельности'

    def __str__(self):
        return self.slogan


class Project(models.Model):
    name = models.ForeignKey(Sphere, on_delete=models.CASCADE)
    prefix_filter = models.CharField('Префикс для фильтра', max_length=3, blank=True,)
    image = models.FileField('Фото', blank=True)


    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = ' Проект'
        verbose_name_plural = ' Проекты'

    def __str__(self):
        return "Фото"


class Testimonial(models.Model):
    name = models.CharField('Имя, фамилия', max_length=50, blank=True)
    testimonial = models.CharField('Отзыв', max_length=800, blank=True)
    image = models.FileField('Фото человека', blank=True)


    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:80px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото человека'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True,)
    phone = models.CharField('Телефон', max_length=50, blank=True, )
    massage = models.TextField('Сообщение', blank=True,)

    class Meta:
        verbose_name = 'Сообщение, заказ'
        verbose_name_plural = 'Сообщения, заказы'

    def __str__(self):
        return self.name
