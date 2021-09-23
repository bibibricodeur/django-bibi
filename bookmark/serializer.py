# https://www.django-rest-framework.org/
# bibibricodeur
# 20210727

from rest_framework import serializers
from .models import BookmarkPost
class BookmarkPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookmarkPost
        fields = '__all__'

### Fin
