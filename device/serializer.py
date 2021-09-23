# https://www.django-rest-framework.org/
# bibibricodeur
# 20210727

from rest_framework import serializers
from .models import DevicePost
class DevicePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicePost
        fields = '__all__'

### Fin
