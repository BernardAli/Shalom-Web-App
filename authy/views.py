from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, reverse
from django.contrib.auth.models import User, auth

from core.models import Auxiliaries, Family, Ministries
from mysite.settings import EMAIL_HOST_USER
from authy.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from main.models import Contribution, Valuations


def register(request, *args, **kwargs):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                subject = 'Congratulations, Account Creation Successful'
                message = f"Hi {username} \n\n\n" \
                          "My name is Reverend Ernest A. Appiah, Head Pastor of Shalom Baptist Church. Thank you" \
                          " for joining the Shalom Baptist family, we’re delighted to have you on board! \n\n" \
                          "Shalom Baptist Church's purpose is to exalt God and to honour our Lord and " \
                          "Saviour Jesus Christ, carry out his command to make disciples of all nations " \
                          "and also teach them to obey all that He commands (Matt 28:18-20) and to grow " \
                          "into maturity.\n\n" \
                          "Thank you, and welcome once again to the Shalom Baptist Church!\n\n\n" \
                          "Ernest A. Appiah,\n" \
                          "Head Pastor,\n" \
                          "Shalom Baptist Church"

                recipient = email

                send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
                messages.success(request, f'Account Creation Successful! Log in here')
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        context = {
            'auxiliaries': auxiliaries,
            'families': families,
            'ministries': ministries,
        }
        return render(request, 'authy/register.html', context)


# @login_required
# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     profile = Profile.objects.get(user=user)
#     # queryset = Contribution.objects.get(member=profile.user.id)
#     # queryset, created = Contribution.objects.get_or_create(member=profile.user, club=user.profile.club)
#     queryset, created = Contribution.objects.get_or_create(member=profile.user, defaults={'club': user.profile.club})
#     # if not queryset:
#     #     queryset = Contribution.objects.create(member=profile.id, club=user.profile.club.id, amount=0)
#     # return queryset
#     investment_value = Valuations.objects.filter(club=user.profile.club).aggregate(Sum('current_value'))
#     contribution_value = Contribution.objects.filter(club=user.profile.club).aggregate(Sum('amount_contribute'), Sum('units'))
#
#     context = {
#         'profile': profile,
#         'queryset': queryset,
#         'investment_value': investment_value,
#         'contribution_value': contribution_value
#     }
#
#     return render(request, 'authy/profile.html', context)

@login_required
def profile(request, username):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    # queryset, created = Contribution.objects.get_or_create(member=profile.user, defaults={'family': user.profile.family})
    context = {
        'profile': profile,
        # 'queryset': queryset,
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }

    return render(request, 'authy/profile.html', context)


def login(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(f'profile', user.username)
            # return redirect(f'home')
        else:
            messages.info(request, "Credentials Invalid")
            return redirect(f'home')
    else:
        context = {
            'auxiliaries': auxiliaries,
            'families': families,
            'ministries': ministries,
        }
        return render(request, 'authy/login.html', context)


def edit_profile(request, username):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            email = user.email
            subject = 'Profile Page Edited'
            message = f'Dear {username} \n\n\n' \
                      'You are receiving this email because your profile details with Shalom Baptist has ' \
                      'been changed.\n\n'\
                      'Kindly reach to us if you did not affect such changes. \n\n\n' \
                      'For more information contact:\n' \
                      '0244526253\n' \
                      '020********\n' \
                      'shalombaptist@gmail.com'

            recipient = email

            admin_email = "manage.archibondsclub@gmail.com"
            # admin_email = "manage.archibondsclub@gmail.com"
            admin_subject = f'{user.username} has updated his/her profile'
            admin_message = f"{user.username} has made changes to his/her profile"

            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            send_mail(admin_subject, admin_message, EMAIL_HOST_USER, [admin_email], fail_silently=False)
            messages.success(request, f'Your account has been updated!')
            return redirect(f'profile', user.username)
        else:
            messages.success(request, f'All fields are required! Make sure you fill all')
            return redirect('edit_profile', user.username)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }

    return render(request, 'authy/edit_profile.html', context)
