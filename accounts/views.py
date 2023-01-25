from django.shortcuts import render
from core.models import Family, Auxiliaries, Ministries
from authy.models import User, Profile

# Create your views here.


def accounts_home(request):
    member_count = User.objects.all().count()
    family_count = Family.objects.all().count()
    auxiliary_count = Auxiliaries.objects.all().count()
    ministry_count = Auxiliaries.objects.all().count()
    context = {
        "member_count": member_count,
        "family_count": family_count,
        'auxiliary_count': auxiliary_count,
        'ministry_count': ministry_count
    }
    return render(request, 'accounts/home.html', context)


def members(request):
    members = Profile.objects.all()
    context = {
        'members': members
    }
    return render(request, 'accounts/member_list.html', context)


def member_details(request, id):
    member = Profile.objects.get(id=id)
    context = {
        'member': member
    }
    return render(request, 'accounts/member_details.html', context)