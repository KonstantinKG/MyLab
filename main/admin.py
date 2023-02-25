from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import *

class CoreSite(admin.AdminSite):
   site_title = "Администрирование сайта"

   site_header = "MyLab"

   index_title = "Администрирование сайта"

core_site = CoreSite(name='Core')

class IndexPageAdmin(admin.ModelAdmin):
   fieldsets = (
      ('Встречающий блок', {
         'fields': ("main_bg", "get_html_main_photo", "hours_text", "out_text"),
      }),
      ('Подготовка к анализам', {
         'fields': ("recommend_p1", "recommend_p2"),
      }),
      ('Контакты', {
         'fields': ("contact_bg", "get_html_contact_photo", ("inst_name", "inst_url"), "email", "phone", "whatsapp", "hire_phone"),
      }),
      ('Адрес', {
         'fields': ("address",),
      }),
   )
   readonly_fields = ("get_html_main_photo", "get_html_contact_photo")

   def get_html_main_photo(self, object):
      if object.main_bg:
         return mark_safe(f"<img src='{object.main_bg.url}' width=100%>")

   def get_html_contact_photo(self, object):
      if object.contact_bg:
         return mark_safe(f"<img src='{object.contact_bg.url}' width=100%>")

   get_html_main_photo.short_description = 'Предпросмотр'
   get_html_contact_photo.short_description = 'Предпросмотр'


core_site.register(IndexPageModel, IndexPageAdmin)

class SaleAdmin(admin.ModelAdmin):
   list_display = ('title',)
   list_display_links = ('title',)
   fields = ("image", "get_html_photo", "title", "text", "details", "date_end", "delete_when_end")
   readonly_fields = ('get_html_photo',)
   search_fields = ("title",)
   list_filter = ("date_end",)

   def get_html_photo(self, object):
      if object.image.image:
         return mark_safe(f"<img src='{object.image.image.url}' width=100%>")
   get_html_photo.short_description = 'Предпросмотр'

core_site.register(SaleModel, SaleAdmin)

class ImagesAdmin(admin.ModelAdmin):
   list_display = ('title', "get_html_photo", "image")
   list_display_links = ('title',)
   list_editable = ("image",)
   fields = ('title', "image", "get_html_photo")
   readonly_fields = ('get_html_photo',)
   search_fields = ("title",)

   def get_html_photo(self, object):
      if object.image:
         return mark_safe(f"<img src='{object.image.url}' width=100%>")
   get_html_photo.short_description = 'Предпросмотр'

core_site.register(ImagesModel, ImagesAdmin)

class ServiceAdmin(admin.ModelAdmin):
   list_display = ('title', "price", "group")
   list_display_links = ('title', "group")
   list_editable = ('price',)
   fields = ("title", "slug", "price", "group")
   prepopulated_fields = {"slug": ("title",)}
   search_fields = ("title",)

core_site.register(ServiceModel, ServiceAdmin)

class ServiceGroupAdmin(admin.ModelAdmin):
   list_display = ('title',)
   list_display_links = ('title',)
   fields = ("title", 'slug')
   prepopulated_fields = {"slug": ("title",)}
   search_fields = ("title",)

core_site.register(ServiceGroupModel, ServiceGroupAdmin)

class PartnersAdmin(admin.ModelAdmin):
   list_display = ('name', 'get_html_photo', 'image')
   list_display_links = ('name',)
   list_editable = ('image',)
   fields = ("name", 'get_html_photo', 'image')
   search_fields = ("name",)
   readonly_fields = ('get_html_photo',)

   def get_html_photo(self, object):
      if object.image:
         return mark_safe(f"<img src='{object.image.url}' width=100%>")
   get_html_photo.short_description = 'Предпросмотр'

core_site.register(PartnersModel, PartnersAdmin)

class VacancyAdmin(admin.ModelAdmin):
   list_display = ('title', 'wage')
   list_display_links = ('title',)
   fields = ("title", "text", "details", "wage")
   search_fields = ('title', 'wage')

core_site.register(VacancyModel, VacancyAdmin)