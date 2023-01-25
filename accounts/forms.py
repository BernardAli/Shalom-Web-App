from django import forms
from django.utils import timezone

from .models import CashFlow, CashFlowHistory


class CashFlowCreateForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['category', 'item_name', 'item_description', 'balance']


class CashFlowUpdateForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['category', 'item_name', 'item_description', 'balance']


class InflowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['received_from', 'amount']


class OutflowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['returned_to', 'receipt_no', 'amount']


class CashFlowHistorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                     required=False, initial=timezone.now)
    end_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                   required=False, initial=timezone.now)

    class Meta:
        model = CashFlowHistory
        fields = ['category', 'item_name', 'export_to_CSV', 'start_date', 'end_date']
