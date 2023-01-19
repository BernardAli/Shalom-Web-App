from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone_no', 'family', 'auxiliary')
    list_filter = ('family', 'auxiliary')
    search_fields = ('user__username', )