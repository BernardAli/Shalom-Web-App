from django import forms
from django.utils import timezone

from .models import InterestedMember, InterestedMemberAcceptance


class InterestedMemberForm(forms.ModelForm):
    class Meta:
        model = InterestedMember
        fields = "__all__"


class InterestedMemberAcceptanceForm(forms.ModelForm):
    class Meta:
        model = InterestedMemberAcceptance
        fields = "__all__"