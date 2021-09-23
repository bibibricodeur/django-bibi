# https://www.django-rest-framework.org/
# bibibricodeur
# 20210727

from rest_framework import serializers
from .models import WikiPost
class WikiPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiPost
        fields = '__all__'

### Fin
