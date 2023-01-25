from django import forms
from django.utils import timezone

from .models import InterestedMember, InterestedMemberAcceptance, Subscribers


class InterestedMemberForm(forms.ModelForm):
    class Meta:
        model = InterestedMember
        fields = "__all__"


class InterestedMemberAcceptanceForm(forms.ModelForm):
    class Meta:
        model = InterestedMemberAcceptance
        fields = "__all__"


class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'box'}), required=True)

    class Meta:
        model = Subscribers
        fields = "__all__"