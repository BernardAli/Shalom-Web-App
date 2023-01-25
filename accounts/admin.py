from django.contrib import admin
from .models import CashFlow, CashFlowHistory, Cash

# Register your models here.


admin.site.register(CashFlow)
admin.site.register(CashFlowHistory)
admin.site.register(Cash)