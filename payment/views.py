from django.core.mail import send_mail
from django.utils.timezone import now
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

from mysite.settings import EMAIL_HOST_USER
from .forms import PaymentForm
from django.conf import settings
from .models import Payment
from django.contrib import messages

# Create your views here.


def initiate_payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, "payment/make_payments.html", {'payment': payment,
                                                          'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = PaymentForm()
    return render(request, "payment/initiate_payments.html", {'payment_form': payment_form})


def verify_payment(request, ref: str):
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    user = request.user
    if verified:
        subject = 'Donation Received'
        full_name = user
        message = f"Contribution Received from {user}"
        recipient = "alibernard.1992@gmail.com"
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        messages.success(request, "Donation Successful")
    else:
        messages.error(request, "Donation Failed")
    return redirect('initiate-payment')