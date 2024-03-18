from django import forms
from subscribe.models import Subscriber
from django.utils.translation import gettext_lazy as _

# def validator_comma(value):
#     if ',' in value:
#         raise forms.validationError("Error, must not contain ','")
#     return value


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        # exclude =('first_name',)
        fields = "__all__"
        labels ={
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email')
        }
        help_texts = {
            'first_name': _('Enter Character only')
        }
        error_messages = {
            'first_name': {
                'required':_('You cannot leave field empty')
            }
        }
# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, required=False, label='First Name', help_text='Enter Characters Only')
#     last_name = forms.CharField(max_length=100, label='Last Name', validators=[validator_comma,])
#     email = forms.EmailField(max_length=100, label='Email')
    
#     # validation method one
#     # def clean_first_name(self):
#     #     data = self.cleaned_data['first_name']
#     #     if ',' in data:
#     #         raise forms.validationError("Invalid First Name")
#     #     return data
    