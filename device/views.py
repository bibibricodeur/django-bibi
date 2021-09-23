#from django.shortcuts import render
# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.http import HttpResponse

# https://docs.djangoproject.com/fr/3.1/intro/tutorial03/
#from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import DevicePost

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the blog index.")
    #template = loader.get_template('blog/index.html')
    context = {
        'posts': DevicePost.objects.filter(device_status='published').filter(device_favorite='True').order_by('device_brand')
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'device/index.html', context)

# https://docs.djangoproject.com/fr/3.1/intro/tutorial04/
from django.urls import reverse
from django.views import generic

class DeviceListView(generic.ListView):
    template_name = 'device/list.html'
    context_object_name = 'posts'
    paginate_by = 18
    def get_queryset(self):
        """Return"""
        return DevicePost.objects.filter(device_status = 'published').order_by('device_brand')

class DeviceDetailView(generic.DetailView):
    model = DevicePost
    template_name = 'device/detail.html'

# https://docs.djangoproject.com/fr/3.2/ref/class-based-views/generic-editing/
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import DeviceCreateForm
class DeviceCreateView(CreateView):
    model = DevicePost
    #fields = '__all__'
    fields = ['device_brand', 'device_model']
    template_name = 'device/create.html'
    success_url = reverse_lazy('device-list')

from django.views.generic.edit import UpdateView

class DeviceUpdateView(UpdateView):
    model = DevicePost
    #fields = '__all__'
    fields = ['device_brand', 'device_model']
    template_name = 'device/update.html'
    success_url = reverse_lazy('device-list')

#from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

class DeviceDeleteView(DeleteView):
    model = DevicePost
    template_name = 'device/delete.html'
    success_url = reverse_lazy('device-list')

### Fin
