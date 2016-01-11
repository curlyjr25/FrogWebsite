from django import forms
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.forms import Form, ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Column, Field, Fieldset, \
    Layout, Row, Submit

from surgery.models import Surgery

class SurgeryForm(ModelForm):
    class Meta:
        model = Surgery
        fields = [
            'surgery_number', 'date', 'frog', 'tank_number', 'collagenase', 
            'collagenase_amount', 'activity', 'solution_volume', 'g_b_oocytes', 
            'volume_of_oocytes', 'previous_surgery', 'company', 
            'number_oocytes_ordered', 'complaints', 'notes',
        ]

    def __init__(self, *args, **kwargs):
        super(SurgeryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('surgery_number', css_class="form-control"),
            Field('date', css_class="form-control"),
            Field('frog', css_class="form-control"),
            Field('tank_number', css_class="form-control"),
            Field('collagenase', css_class="form-control"),
            Field('collagenase_amount', css_class="form-control"),
            Field('activity', css_class="form-control"),
            Field('solution_volume', css_class="form-control"),
            Field('g_b_oocytes', css_class="form-control"),
            Field('volume_of_oocytes', css_class="form-control"),
            Field('previous_surgery', css_class="form-control"),
            Field('company', css_class="form-control"),
            Field('number_oocytes_ordered', css_class="form-control"),
            Field('complaints', css_class="form-control"),
            Field('notes', css_class="form-control"),
        )
        self.helper.form_tag = False

