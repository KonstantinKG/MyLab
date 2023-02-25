from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', cache_page(60*15)(IndexView.as_view()), name='index'),
   path('search/', cache_page(60*15)(SearchDataView.as_view()), name='search'),
]