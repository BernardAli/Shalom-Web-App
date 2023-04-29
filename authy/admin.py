from django.contrib import admin
from .models import Profile, Employees, Position, OfficeHours


# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'phone_no', 'family', 'auxiliary')
    list_filter = ('family', 'auxiliary')
    search_fields = ('user__username',)


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_no', 'email', 'place_of_residence')
    list_filter = ('gender', 'marital_status')
    search_fields = ('full_name',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary', 'appointed_date')
    list_filter = ('position',)
    search_fields = ('name',)


@admin.register(OfficeHours)
class OfficeHoursAdmin(admin.ModelAdmin):
    list_display = ('position', 'office_hours', 'office_days', 'at_office')
    list_filter = ('position', 'office_days')
