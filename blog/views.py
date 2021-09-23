#from django.shortcuts import render
# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.http import HttpResponse

# https://docs.djangoproject.com/fr/3.1/intro/tutorial03/
#from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import BlogPost

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the blog index.")
    #template = loader.get_template('blog/index.html')
    context = {
        'posts': BlogPost.objects.filter(blog_status='published').filter(blog_favorite='True').order_by('blog_title')
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'blog/index.html', context)

# https://docs.djangoproject.com/fr/3.1/intro/tutorial04/
from django.urls import reverse
from django.views import generic

class BlogListView(generic.ListView):
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 18
    def get_queryset(self):
        """Return"""
        return BlogPost.objects.filter(blog_status = 'published').order_by('blog_title')

class BlogDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'

# https://docs.djangoproject.com/fr/3.2/ref/class-based-views/generic-editing/
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import BlogCreateForm

class BlogCreateView(CreateView):
    model = BlogPost
    #fields = '__all__'
    fields = ['blog_title', 'blog_description', 'blog_content']
    #form_class = BlogCreateForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog-list')

#from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

class BlogUpdateView(UpdateView):
    model = BlogPost
    #fields = '__all__'
    fields = ['blog_title', 'blog_description', 'blog_content', 'blog_category']
    template_name = 'blog/update.html'
    success_url = reverse_lazy('blog-list')

#from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog-list')

### Fin
