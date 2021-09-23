#from django.shortcuts import render
# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.http import HttpResponse

# https://docs.djangoproject.com/fr/3.1/intro/tutorial03/
#from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import BookmarkPost

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the blog index.")
    #template = loader.get_template('blog/index.html')
    context = {
        'posts': BookmarkPost.objects.filter(bookmark_status='published').filter(bookmark_favorite='True').order_by('bookmark_title')
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'bookmark/index.html', context)

# https://docs.djangoproject.com/fr/3.1/intro/tutorial04/
from django.urls import reverse
from django.views import generic

class BookmarkListView(generic.ListView):
    template_name = 'bookmark/list.html'
    context_object_name = 'posts'
    paginate_by = 18
    def get_queryset(self):
        """Return"""
        return BookmarkPost.objects.filter(bookmark_status = 'published').order_by('bookmark_title')

class BookmarkDetailView(generic.DetailView):
    model = BookmarkPost
    template_name = 'bookmark/detail.html'

# https://docs.djangoproject.com/fr/3.2/ref/class-based-views/generic-editing/
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import BookmarkCreateForm
class BookmarkCreateView(CreateView):
    model = BookmarkPost
    #fields = '__all__'
    fields = ['bookmark_title', 'bookmark_description']
    template_name = 'bookmark/create.html'
    success_url = reverse_lazy('bookmark-list')

from django.views.generic.edit import UpdateView

class BookmarkUpdateView(UpdateView):
    model = BookmarkPost
    #fields = '__all__'
    fields = ['bookmark_title', 'bookmark_description']
    template_name = 'bookmark/update.html'
    success_url = reverse_lazy('bookmark-list')

#from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

class BookmarkDeleteView(DeleteView):
    model = BookmarkPost
    template_name = 'bookmark/delete.html'
    success_url = reverse_lazy('bookmark-list')

### Fin
