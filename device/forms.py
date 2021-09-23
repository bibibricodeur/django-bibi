# https://docs.djangoproject.com/fr/3.1/topics/forms/
# https://docs.djangoproject.com/fr/3.1/topics/forms/modelforms/
from django import forms
#from django.forms import ModelForm
from .models import DevicePost

class DeviceCreateForm(forms.Form):
    device_brand = forms.CharField(label='Brand', max_length=255)
    device_model = forms.CharField(label='Model', max_length=255)
    #pass

class DeviceUpdateForm(forms.Form):
    pass

## Fin
