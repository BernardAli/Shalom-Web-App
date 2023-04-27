from django.contrib import admin
from .models import Payment

# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'email', 'verified', 'description')
    list_filter = ('verified', 'email', 'amount', )
    search_fields = ('amount', )