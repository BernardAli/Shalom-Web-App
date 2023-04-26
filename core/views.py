from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from accounts.models import CashFlowHistory
from mysite.settings import EMAIL_HOST_USER
from .models import InterestedMember, InterestedMemberAcceptance, Auxiliaries, Family, Ministries, \
    AuxiliaryMeetings, UpcomingEvents, AuxiliaryExecutives, FAQ, AuxiliariesFAQ, FamilyFAQ, Subscribers, \
    Services, Sermon, Subscribers, Gallery, GalleryCategory, Testimony
from .forms import InterestedMemberForm, InterestedMemberAcceptanceForm, SubscribeForm
from authy.models import User, Profile


# Create your views here.


def home_page(request):
    faqs = FAQ.objects.all()
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    services = Services.objects.all()
    upcoming_events = UpcomingEvents.objects.filter(completed=False)
    testimonials = Testimony.objects.all()
    member_count = User.objects.all().count()

    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Thanks for subscribing to Real Estates'
            message = "We'll update you on all latest developments"
            recipient = form.cleaned_data.get('email')
            # print(recipient)
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            form = Subscribers.objects.create(email=recipient)
            form.save()
            messages.success(request, f'Subscription successful!')
        else:
            sub = SubscribeForm(request.POST)

    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        message = f"Name: {name} \n" \
                  f"Number: {number} \n" \
                  f"Email: {email} \n" \
                  f"Message: {message}"

        recipient = EMAIL_HOST_USER

        send_mail(subject, message, email, [recipient], fail_silently=False)
        messages.success(request, f'Message Successfully sent')
        return redirect("home")

    context = {
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
        'upcoming_events': upcoming_events,
        'faqs': faqs,
        'services': services,
        'testimonials': testimonials,
        "member_count": member_count
    }
    return render(request, 'core/home.html', context)


def history(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    context = {
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }
    return render(request, 'core/history.html', context)


def branches(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    context = {
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }
    return render(request, 'core/branches.html', context)


def members(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    members = Profile.objects.all()
    context = {
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
        'members': members
    }
    return render(request, 'core/members.html', context)


def service_details(request, id):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    service = get_object_or_404(Services, pk=id)
    sermons = Sermon.objects.filter(service=service)
    context = {
        'service': service,
        'sermons': sermons,
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }
    return render(request, 'core/service_details.html', context)


def subscribers(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Thanks for subscribing to Shalom Baptist Church'
            message = "We'll update you on all latest developments"
            recipient = form.cleaned_data.get('email')
            # print(recipient)
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            if Subscribers.objects.filter(email=recipient).exists():
                messages.success(request, f'Already subscribed!')
            else:
                form = Subscribers.objects.create(email=recipient)
                form.save()
                messages.success(request, f'Subscription successful!')
        else:
            sub = SubscribeForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'core/home.html', context)


def gallery(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    gallery_cat = GalleryCategory.objects.all()
    galleries = Gallery.objects.all()

    context = {
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
        'galleries': galleries,
        'gallery_cat': gallery_cat
    }
    return render(request, 'core/gallery.html', context)


def ministries(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()

    context = {
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries
    }
    return render(request, 'core/ministries.html', context)


def families(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()

    context = {
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries
    }
    return render(request, 'core/families.html', context)


def aux_details(request, id):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    auxiliary = get_object_or_404(Auxiliaries, pk=id)
    meeting_time = AuxiliaryMeetings.objects.get(auxiliary=auxiliary.id)
    executives = AuxiliaryExecutives.objects.filter(auxiliary=auxiliary.id)
    faqs = AuxiliariesFAQ.objects.filter(auxiliary=auxiliary.id)
    context = {
        'auxiliary': auxiliary,
        'meeting_time': meeting_time,
        'executives': executives,
        'faqs': faqs,
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }
    return render(request, 'core/auxiliary_detail.html', context)


def fam_details(request, id):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    family = get_object_or_404(Family, pk=id)
    faqs = FamilyFAQ.objects.filter(family=family.id)
    context = {
        'family': family,
        'faqs': faqs,
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }
    return render(request, 'core/family_detail.html', context)


def min_details(request, id):
    ministry = Ministries.objects.get(id=id)
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    context = {
        'ministry': ministry,
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }
    return render(request, 'core/ministry_detail.html', context)


def join_view(request):
    ministries = Ministries.objects.all()
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
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
        'form': form,
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
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
                          f"Create your account with this link https://shalombaptist.pythonanywhere.com/register/\n\n" \
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


def subscribers_mail(request):
    subscribers = Subscribers.objects.all()
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        file = request.POST['file']

        message = f"Message: {message}"
        # message.attach(file)

        recipient = EMAIL_HOST_USER

        # send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)

        email = EmailMessage(
            subject,
            message,
            EMAIL_HOST_USER,
            to=[[subs.email] for subs in subscribers.all()],
            headers={'Message-ID': 'foo'},
        )
        # email.attach(file)
        email.send(fail_silently=False)

        messages.success(request, f'Message Successfully sent')
        return redirect("home")

    return render(request, 'core/sub_mail.html')


def deacons_view(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    deacons = Profile.objects.filter(is_deacon=True)
    context = {
        'deacons': deacons,
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }
    return render(request, 'core/deacons.html', context)


def council_view(request):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    councils = Profile.objects.filter(is_council_member=True)
    context = {
        'councils': councils,
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
    }
    return render(request, 'core/councils.html', context)


class CreateTestimonyView(CreateView):
    model = Testimony
    fields = "__all__"
    template_name = 'core/create_testimony.html'
    success_url = 'home'


def statements(request, id):
    auxiliaries = Auxiliaries.objects.all()
    families = Family.objects.all()
    ministries = Ministries.objects.all()
    member = Profile.objects.get(id=id)
    payments = CashFlowHistory.objects.filter(received_from=member)

    context = {
        'auxiliaries': auxiliaries,
        'families': families,
        'ministries': ministries,
        'payments': payments,
        'member': member
    }
    return render(request, 'core/statements.html', context)
