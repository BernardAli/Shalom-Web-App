from django.contrib import admin
from .models import InterestedMember, InterestedMemberAcceptance, Family, Auxiliaries

# Register your models here.


admin.site.register(InterestedMember)
admin.site.register(InterestedMemberAcceptance)
admin.site.register(Family)
admin.site.register(Auxiliaries)