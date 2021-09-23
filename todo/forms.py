# https://docs.djangoproject.com/fr/3.2/topics/forms/
# https://docs.djangoproject.com/fr/3.2/topics/forms/modelforms/
from django import forms
#from django.forms import ModelForm
from .models import TodoPost

# https://docs.djangoproject.com/fr/3.2/ref/forms/widgets/

class TodoCreateForm(forms.Form):
    todo_title = forms.CharField(label='Title forms', widget=forms.TextInput(attrs={'class': 'input-field col s12'}))
    todo_description = forms.CharField(label='Description forms', widget=forms.TextInput(attrs={'class': 'input-field col s12'}))
    todo_content = forms.Textarea()
    #pass

class TodoUpdateForm(forms.Form):
    pass

## Fin
