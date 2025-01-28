from django import forms
from django_jalali.forms import jDateField,jDateTimeField
from django_jalali.admin.widgets import AdminjDateWidget,AdminSplitjDateTime
from app.models import typev,typem,padcast,test,question,answer,image,vidio
from datetime import datetime
from django.core.exceptions import ValidationError


class AppointmentForm(forms.Form):
    date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    time = forms.ChoiceField(
         required=True
    )
    appointment_type = forms.ChoiceField(
        label="نوع رزرو",
        choices=[("online", "آنلاین"), ("offline", "حضوری")]
    )
    status=forms.ChoiceField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'status'}),
    )
 