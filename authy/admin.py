from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone', 'family', 'auxiliaries')
    list_filter = ('family', 'auxiliaries')
    search_fields = ('first_name', 'last_name', 'user__username')