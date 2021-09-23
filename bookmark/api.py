# https://www.django-rest-framework.org/
# bibibricodeur
# 20210727

from rest_framework import generics
from rest_framework.response import Response
from .serializer import BookmarkPostSerializer
from .models import BookmarkPost

class BookmarkPostApi(generics.ListCreateAPIView):
    queryset = BookmarkPost.objects.all()
    serializer_class = BookmarkPostSerializer

### Fin
