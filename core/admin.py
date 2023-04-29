from django.contrib import admin
from .models import InterestedMember, InterestedMemberAcceptance, Family, Auxiliaries, Ministries, \
    AuxiliaryMeetings, UpcomingEvents, AuxiliaryExecutives, FAQ, AuxiliariesFAQ, FamilyFAQ, Subscribers, \
    Services, Sermon, GalleryCategory, Gallery, Testimony, Books, BooksCategory

# Register your models here.


admin.site.register(InterestedMember)
admin.site.register(InterestedMemberAcceptance)
admin.site.register(Family)


@admin.register(Auxiliaries)
class AuxiliariesAdmin(admin.ModelAdmin):
    list_display = ('name', 'contribution_target')


admin.site.register(Ministries)
admin.site.register(AuxiliaryMeetings)


@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    list_display = ('event', 'date', 'completed')
    list_filter = ('completed',)


@admin.register(AuxiliaryExecutives)
class AuxiliaryExecutivesAdmin(admin.ModelAdmin):
    list_display = ('auxiliary', 'full_name', 'position', 'phone_no')
    list_filter = ('auxiliary',)
    search_fields = ('full_name',)


admin.site.register(FAQ)
admin.site.register(AuxiliariesFAQ)
admin.site.register(FamilyFAQ)
admin.site.register(Subscribers)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'times', 'days')


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('service', 'preacher', 'title', 'date')
    list_filter = ('service', 'preacher')


admin.site.register(GalleryCategory)
admin.site.register(Gallery)


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'author')
    list_filter = ('category', 'author')
    search_fields = ('author', )


admin.site.register(BooksCategory)
admin.site.register(Testimony)
