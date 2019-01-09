from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Subscription


# class SubscriptionForm(forms.ModelForm):
#
#     class Meta:
#         model = Subscription


class VisitReportForm(forms.Form):
    date = forms.DateField(
        widget=DatePickerInput(format='%Y-%m-%d')
    )
