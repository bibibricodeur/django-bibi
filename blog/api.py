# https://www.django-rest-framework.org/
# bibibricodeur
# 20210727

from rest_framework import generics
from rest_framework.response import Response
from .serializer import BlogPostSerializer
from .models import BlogPost

class BlogPostApi(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

### Fin
