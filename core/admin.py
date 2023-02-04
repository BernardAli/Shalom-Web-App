from django.contrib import admin
from .models import InterestedMember, InterestedMemberAcceptance, Family, Auxiliaries, Ministries, \
    AuxiliaryMeetings, UpcomingEvents, AuxiliaryExecutives, FAQ, AuxiliariesFAQ, FamilyFAQ, Subscribers, \
    Services, Sermon, GalleryCategory, Gallery

# Register your models here.


admin.site.register(InterestedMember)
admin.site.register(InterestedMemberAcceptance)
admin.site.register(Family)
admin.site.register(Auxiliaries)
admin.site.register(Ministries)
admin.site.register(AuxiliaryMeetings)
admin.site.register(UpcomingEvents)
admin.site.register(AuxiliaryExecutives)
admin.site.register(FAQ)
admin.site.register(AuxiliariesFAQ)
admin.site.register(FamilyFAQ)
admin.site.register(Subscribers)
admin.site.register(Services)
admin.site.register(Sermon)
admin.site.register(GalleryCategory)
admin.site.register(Gallery)