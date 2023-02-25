import phonenumbers
from django.db import models
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError

class IndexPageModel(models.Model):
   main_bg = models.ImageField(upload_to="index", blank=True, verbose_name='Фоновое изображение')
   hours_text = models.CharField(max_length=22, verbose_name='Часы работы')
   out_text = models.CharField(max_length=22, verbose_name='Выезд на дом')

   recommend_p1 = models.TextField(verbose_name='Параграф 1-й')
   recommend_p2 = models.TextField(verbose_name='Параграф 2-й')

   contact_bg = models.ImageField(upload_to="index", blank=True, verbose_name='Фоновое изображение контактов')
   inst_name = models.CharField(max_length=30, blank=True, verbose_name='Название Инстаграма')
   inst_url = models.URLField(blank=True, verbose_name='Ссылка на Инстаграм')
   email = models.EmailField(blank=True, verbose_name='Почта')
   phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
   whatsapp = models.CharField(max_length=20, blank=True, verbose_name='Телефон Whatsapp')
   hire_phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон отдела кадров')

   address = models.CharField(max_length=255, blank=True, verbose_name='Адрес')

   class Meta:
      verbose_name = 'Найстройку главной страницы'
      verbose_name_plural = 'Главная страница'

   def get_formatted_number(self, phone):
      try:
         parsed_phone = phonenumbers.parse(self.phone, "KZ")
         return phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.NATIONAL)
         Meta.verbose_name
      except:
         return "телефон"

   def get_formatted_phone(self):
      return self.get_formatted_number(self.phone)

   def get_formatted_hire_phone(self):
      return self.get_formatted_number(self.hire_phone)

   def get_formatted_whatsapp_phone(self):
      return self.get_formatted_number(self.whatsapp)

   def __str__(self):
      return "Настроить главную страницу"

   def clean(self):
      exist_model = IndexPageModel.objects.first()
      if exist_model and exist_model.pk != self.pk:
         raise ValidationError({'__all__': 'Невозможно создать вторую запись.'})
      super(IndexPageModel, self).clean()



class SaleModel(models.Model):
   image = models.ForeignKey('ImagesModel', on_delete=models.PROTECT, default='', verbose_name='Изображение')
   title = models.CharField(max_length=12, verbose_name='Заголовок акции', help_text='Максимальная длина 12 символов')
   text = models.TextField(max_length=60, verbose_name='Краткое описание')
   details = models.TextField(max_length=300, blank=True, verbose_name='Подробное описание')
   date_end = models.DateField(blank=True, verbose_name='Дата окончания')
   delete_when_end = models.BooleanField(default=False, verbose_name='Удалить по окончанию')

   class Meta:
      verbose_name = 'Акция'
      verbose_name_plural = 'Акции'
      ordering = ['id']

   def __str__(self):
      return self.title

   def save(self, *args, **kwargs):
      if not self.id:
         self.image = self.compressImage(self.image)
      super(SaleModel, self).save(*args, **kwargs)

class ImagesModel(models.Model):
   title = models.CharField(max_length=64, verbose_name='Дайте название изображению чтобы легче его найти')
   image = models.ImageField(upload_to="shared/", null=True, blank=True, verbose_name='Изображение')

   class Meta:
      verbose_name = 'Изображение'
      verbose_name_plural = 'Общие изображения'
      ordering = ['id']

   def __str__(self):
      return f'{self.title} | {self.image.url}'



class ServiceModel(models.Model):
   title = models.CharField(max_length=255, verbose_name='Название')
   slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
   price = models.SmallIntegerField(verbose_name='Стоимость')
   group = models.ForeignKey('ServiceGroupModel', on_delete=models.CASCADE, related_name='services', verbose_name='Группа')

   class Meta:
      verbose_name = 'Услугу'
      verbose_name_plural = 'Услуги'
      ordering = ['group']

   def __str__(self):
      return self.title

class ServiceGroupModel(models.Model):
   title = models.CharField(max_length=255, verbose_name='Название')
   slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

   class Meta:
      verbose_name = 'Группа для услуг'
      verbose_name_plural = 'Группы для услуг'
      ordering = ['id']

   def __str__(self):
      return self.title

class PartnersModel(models.Model):
   name = models.CharField(max_length=255, verbose_name='Название')
   image = models.ImageField(upload_to="partners/", null=True, blank=True, verbose_name='Логотип')

   class Meta:
      verbose_name = 'Партнер'
      verbose_name_plural = 'Партнеры'
      ordering = ['id']

   def __str__(self):
      return self.name



class VacancyModel(models.Model):
   title = models.CharField(max_length=30, verbose_name='Заголовок вакансии', help_text='Максимальная длина 12 символов')
   text = models.TextField(max_length=60, verbose_name='Краткое описание')
   wage = models.SmallIntegerField(default=0, verbose_name='Зарплата')
   details = models.TextField(max_length=300, blank=True, verbose_name='Подробное описание')

   class Meta:
      verbose_name = 'Вакансия'
      verbose_name_plural = 'Вакансии'
      ordering = ['id']

   def __str__(self):
      return self.title