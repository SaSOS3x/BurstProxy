from statistics import mode
from django.db import models

class Ip(models.Model): # наша таблица где будут айпи адреса
    ip = models.CharField(max_length=100)
    

    def __str__(self):
        return self.ip
    


class News(models.Model):
    # id = models.IntegerField(default=0, primary_key=True, unique=True)
    title = models.CharField('Название', max_length=250)
    short_text = models.CharField('Текст', max_length=250)
    date =models.DateTimeField('Дата публикации')

    
    view_id = models.ManyToManyField(Ip, related_name='views', blank=True)
    view_count = models.IntegerField(default=0)

    photo = models.CharField('Фото: номер записи', max_length=250)

    tag_firefox = models.BooleanField('Tag_Fierfox', default=0)
    tag_Opera = models.BooleanField('Tag_Opera', default=0)
    tag_tarifs = models.BooleanField('Tag_Tarifs', default=0)
    tag_multiport = models.BooleanField('Tag_multiport', default=0)
    tag_yandex = models.BooleanField('Tag_yandex', default=0)

    categories_arbitraj = models.BooleanField('Fierfox', default=0)
    categories_nocontent = models.BooleanField('Без рубрики', default=0)
    categories_mobileproxy = models.BooleanField('Мобильные прокси', default=0)
    categories_settingsproxy = models.BooleanField('Настройки прокси', default=0)
    categories_aboutproxy = models.BooleanField('О прокси', default=0)
    categories_moneysystem = models.BooleanField('Платёжные системы', default=0)
    categories_tarifs = models.BooleanField('Тарифы', default=0)

    include_templates = models.CharField('Название шаблона', max_length=250)

    def total_views(self):
        return self.view_id.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

class Categories(models.Model):
    title = models.CharField('Название', max_length=250)
    code = models.CharField('Название в коде', max_length=250, default='none')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tags(models.Model):
    title = models.CharField('Название', max_length=250)
    code = models.CharField('Название в коде', max_length=250, default='none')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'