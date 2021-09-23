#from django.shortcuts import render
# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.http import HttpResponse

# https://docs.djangoproject.com/fr/3.1/intro/tutorial03/
#from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import WikiPost

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the blog index.")
    #template = loader.get_template('blog/index.html')
    context = {
        'posts': WikiPost.objects.filter(wiki_status='published').filter(wiki_favorite='True').order_by('wiki_title')
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'wiki/index.html', context)

# https://docs.djangoproject.com/fr/3.1/intro/tutorial04/
from django.urls import reverse
from django.views import generic

class WikiListView(generic.ListView):
    template_name = 'wiki/list.html'
    context_object_name = 'posts'
    paginate_by = 18
    def get_queryset(self):
        """Return"""
        return WikiPost.objects.filter(wiki_status = 'published').order_by('wiki_title')

class WikiDetailView(generic.DetailView):
    model = WikiPost
    template_name = 'wiki/detail.html'

### Fin
