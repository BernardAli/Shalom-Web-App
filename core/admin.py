from django.contrib import admin
from .models import InterestedMember, InterestedMemberAcceptance, Family, Auxiliaries, Ministries, \
    AuxiliaryMeetings, UpcomingEvents

# Register your models here.


admin.site.register(InterestedMember)
admin.site.register(InterestedMemberAcceptance)
admin.site.register(Family)
admin.site.register(Auxiliaries)
admin.site.register(Ministries)
admin.site.register(AuxiliaryMeetings)
admin.site.register(UpcomingEvents)