from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Модель', max_length=50)
    price = models.IntegerField('Цена')
    image = models.ImageField('Картинка')
    release_date = models.DateField('Дата релиза')
    lte_exists = models.BooleanField('Наличие LTE')
    slug = models.SlugField('Идентификатор')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Phone, self).save(*args, **kwargs)