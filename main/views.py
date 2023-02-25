import json
from .models import *
from django.db.models import F, Q
from django.http import JsonResponse
from django.views.generic import View, TemplateView

class IndexView(TemplateView):
   template_name = 'index.html'

   def get(self, request, *args, **kwargs):
      return super().get(request, args, kwargs)

   def get_context_data(self, *, object_list=None, **kwargs):
      return super().get_context_data(
         page = IndexPageModel.objects.first(),
         sales = SaleModel.objects.all(),
         catalog = ServiceGroupModel.objects.all().prefetch_related('services'),
         partners = PartnersModel.objects.all(),
         vacancies = VacancyModel.objects.all(),

         **kwargs
      )

class SearchDataView(View):
   def get(self, request, *args, **kwargs):
      points = ServiceModel.objects.values('title', 'slug').all()
      subpoints = ServiceGroupModel.objects.values('title', 'slug').all()
      data = list(points) + list(subpoints)

      return JsonResponse({"data": data}, json_dumps_params={'ensure_ascii': False})