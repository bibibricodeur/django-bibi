# https://docs.djangoproject.com/fr/3.2/topics/forms/
# https://docs.djangoproject.com/fr/3.2/topics/forms/modelforms/
from django import forms
#from django.forms import ModelForm
from .models import BookmarkPost

# https://docs.djangoproject.com/fr/3.2/ref/forms/widgets/

class BookmarkCreateForm(forms.Form):
    bookmark_title = forms.CharField(label='Title', max_length=255)
    bookmark_uri = forms.CharField(label='URI', max_length=255)
    bookmark_description = forms.CharField(label='Description', max_length=255)
    bookmark_category = forms.CharField(label='Category', max_length=255)
    #pass

class DeviceUpdateForm(forms.Form):
    pass

## Fin
