from django.shortcuts import render

from core.models import Auxiliaries, Family, Ministries


def assets(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    context = {
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }
    return render(request, 'assets/assets.html', context)
