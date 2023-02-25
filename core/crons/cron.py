from main.models import SaleModel
from datetime import date, timezone

def clearExpiredSales():
   SaleModel.objects.filter(delete_when_end=True, date_end__lte=date.today()).delete()