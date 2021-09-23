# https://www.django-rest-framework.org/
# bibibricodeur
# 20210727

from rest_framework import generics
from rest_framework.response import Response
from .serializer import WikiPostSerializer
from .models import WikiPost

class WikiPostApi(generics.ListCreateAPIView):
    queryset = WikiPost.objects.all()
    serializer_class = WikiPostSerializer

### Fin
