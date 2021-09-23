# https://www.django-rest-framework.org/
# bibibricodeur
# 20210727

from rest_framework import generics
from rest_framework.response import Response
from .serializer import DevicePostSerializer
from .models import DevicePost

class DevicePostApi(generics.ListCreateAPIView):
    queryset = DevicePost.objects.all()
    serializer_class = DevicePostSerializer

### Fin
