from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from mysite.settings import EMAIL_HOST_USER
from .models import InterestedMember, InterestedMemberAcceptance, Auxiliaries, Family, Ministries, \
    AuxiliaryMeetings, UpcomingEvents
from .forms import InterestedMemberForm, InterestedMemberAcceptanceForm

# Create your views here.


def home_page(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    upcoming_events = UpcomingEvents.objects.filter(completed=False)
    context = {
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries
    }
    return render(request, 'core/home.html', context)


def gallery(request):
    return render(request, 'core/gallery.html')


def aux_details(request, id):
    auxiliary = get_object_or_404(Auxiliaries, pk=id)
    meeting_time = AuxiliaryMeetings.objects.get(auxiliary=auxiliary.id)
    context = {
        'auxiliary': auxiliary,
        'meeting_time': meeting_time
    }
    return render(request, 'core/auxiliary_detail.html', context)


def fam_details(request, id):
    family = Family.objects.get(id=id)
    context = {
        'family': family
    }
    return render(request, 'core/family_detail.html', context)


def min_details(request, id):
    ministry = Ministries.objects.get(id=id)
    context = {
        'ministry': ministry
    }
    return render(request, 'core/ministry_detail.html', context)


def join_view(request):
    form = InterestedMemberForm()
    if request.method == 'POST':
        form = InterestedMemberForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            contact = form.cleaned_data.get('contact')
            member_status = form.cleaned_data.get('member_status')
            recipient = form.cleaned_data.get('email')
            admin_email = "alibernard.1992@gmail.com"

            first_name = full_name.split(" ")[0]
            subject = 'Welcome to Shalom Baptist Family'
            message = f"Hello {first_name}, \n\n" \
                      f"We’re excited that you’ve taken the first step towards joining the Shalom Baptist family – " \
                      f"the world’s best Bible believing church. \n\n" \
                      f"You still need to complete the rest of your application, but to make it easy for you to resume " \
                      f"your application all you need to do is to relax. \n\n" \
                      f"An officer will call you within 24hours to assist you " \
                      f"and answer most of the questions you may have \n\n" \
                      f"We can’t wait to welcome you on board as a member of " \
                      f"the Shalom Baptist family. \n\n\n" \
                      f"With regards, \n" \
                      f"Your family at Shalom Baptist"

            admin_subject = 'New Member is Interested'
            admin_message = f"The details are: \n" \
                            f"Full Name: {full_name} \n" \
                            f"Number: {contact} \n" \
                            f"Email: {recipient} \n"

            # print(recipient)
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            send_mail(admin_subject, admin_message, EMAIL_HOST_USER, [admin_email], fail_silently=False)
            form = InterestedMember.objects.create(full_name=full_name, contact=contact,
                                                   email=recipient, member_status=member_status)
            form.save()
            messages.success(request, f'Details sent successfully!, Kindly check your email')
            return redirect("home")
        else:
            form = InterestedMemberForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'core/join.html', context)


def join_accepted(request):
    form = InterestedMemberAcceptanceForm()
    if request.method == 'POST':
        form = InterestedMemberAcceptanceForm(request.POST)
        if form.is_valid():
            member = form.cleaned_data.get('member')
            recipient = member.email
            status = form.cleaned_data.get('status')
            admin_email = "alibernard.1992@gmail.com"

            if status == 'Accept':
                first_name = member.full_name.split(" ")[0]
                subject = 'Welcome to Shalom Baptist family'
                message = f"Hello {first_name}, \n\n" \
                          f"Your application has been accepted! You're just a few steps from joining the world's best " \
                          f"Bible Believing Church. \n\n" \
                          f"1. Create your account \n" \
                          f"To create your account, please click on the link below to submit your username and create " \
                          f"a unique password for your account.\n" \
                          f"Create your account with this link http://127.0.0.1:8000/register/\n\n" \
                          f"2. Update your profile \n" \
                          f"After successfully creating your login details, kindly login on the website and Update " \
                          f"your profile.\n\n" \
                          f"That's it!\n\n\n" \
                          f"Any questions? \n" \
                          f"If you have further questions, our friendly Member Happiness Team is always ready to help. " \
                          f"Simply Get in touch!\n\n\n" \
                          f"Once again, thanks for choosing Shalom Baptist!\n\n" \
                          f"With regards, \n" \
                          f"Your family at Shalom Baptist"

                admin_subject = 'New member accepted successfully'
                admin_message = f"{member} has received registration form"

                # print(recipient)
                send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
                send_mail(admin_subject, admin_message, EMAIL_HOST_USER, [admin_email], fail_silently=False)

            else:
                subject = 'Membership Rejected'
                message = f"Sorry, Your application to join Shalom Baptist has been rejected\n"

                admin_subject = 'New member rejected'
                admin_message = f"Rejection email sent successfully"

                # print(recipient)
                send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
                send_mail(admin_subject, admin_message, EMAIL_HOST_USER, [admin_email], fail_silently=False)

            form = InterestedMemberAcceptance.objects.create(member=member, status=status)
            form.save()
            messages.success(request, f'Details sent successfully!')
            return redirect("home")
        else:
            form = InterestedMemberAcceptanceForm(request.POST)

    context = {
        'form': form,
    }
    return render(request, 'core/join_accepted.html', context)