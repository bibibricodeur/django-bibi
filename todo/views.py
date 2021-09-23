#from django.shortcuts import render
# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.http import HttpResponse

# https://docs.djangoproject.com/fr/3.1/intro/tutorial03/
#from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import TodoPost

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the blog index.")
    #template = loader.get_template('blog/index.html')
    context = {
        'todos': TodoPost.objects.filter(todo_status='published').filter(todo_favorite='True').order_by('todo_title')
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'todo/index.html', context)

# https://docs.djangoproject.com/fr/3.1/intro/tutorial04/
from django.urls import reverse
from django.views import generic

class TodoListView(generic.ListView):
    template_name = 'todo/list.html'
    context_object_name = 'todos'
    paginate_by = 18
    def get_queryset(self):
        """Return"""
        return TodoPost.objects.filter(todo_status = 'published').order_by('todo_title')

class TodoDetailView(generic.DetailView):
    model = TodoPost
    template_name = 'todo/detail.html'

# https://docs.djangoproject.com/fr/3.2/ref/class-based-views/generic-editing/
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import TodoCreateForm

class TodoCreateView(CreateView):
    model = TodoPost
    #fields = '__all__'
    fields = ['todo_title', 'todo_description', 'todo_content']
    #form_class = TodoCreateForm
    template_name = 'todo/create.html'
    success_url = reverse_lazy('todo-list')

#from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

class TodoUpdateView(UpdateView):
    model = TodoPost
    #fields = '__all__'
    fields = ['todo_title', 'todo_description', 'todo_content']
    template_name = 'toido/update.html'
    success_url = reverse_lazy('todo-list')

#from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

class TodoDeleteView(DeleteView):
    model = TodoPost
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('todo-list')

### Fin
