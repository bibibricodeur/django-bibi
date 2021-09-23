# https://docs.djangoproject.com/fr/3.2/topics/forms/
# https://docs.djangoproject.com/fr/3.2/topics/forms/modelforms/
from django import forms
#from django.forms import ModelForm
from .models import BlogPost

# https://docs.djangoproject.com/fr/3.2/ref/forms/widgets/

class BlogCreateForm(forms.Form):
    #blog_title = forms.CharField(label='Title forms', widget=forms.TextInput(attrs={'class': 'input-field col s12'}))
    #blog_description = forms.CharField(label='Description forms', widget=forms.TextInput(attrs={'class': 'input-field col s12'}))
    #blog_content = forms.Textarea()
    pass

class BlogUpdateForm(forms.Form):
    pass

## Fin
