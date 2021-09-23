# https://www.django-rest-framework.org/
# bibibricodeur
# 20210727

from rest_framework import serializers
from .models import BlogPost
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

### Fin
