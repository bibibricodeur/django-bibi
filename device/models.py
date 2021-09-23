from django.db import models

# https://docs.djangoproject.com/fr/3.1/intro/tutorial02/

# Cette fonction est utilisée pour formater les URL
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

class DeviceCategory(models.Model):
    # Fields
    category_name = models.CharField('Category', max_length=255, unique=True, blank=True, null=True)

    # https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models

    # Metadata
    class Meta:
        verbose_name = 'Device Category'
        verbose_name_plural = 'Devices Categories'

    # Methods
    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('device-detail', args=[str(self.id)])

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets dans la base de données."""
        return self.device_brand

class DevicePost(models.Model):
    # Fields
    options = (
        ('draft', 'Private'),
        ('published', 'Public'),
    )
    device_brand = models.CharField('Brand', max_length=255, blank=True, null=True)
    device_model = models.CharField('Model', max_length=255, blank=True, null=True)
    device_licence = models.CharField('Licence',max_length=255, blank=True, null=True)
    device_bridge = models.CharField('Bridge', max_length=255, blank=True, null=True)
    device_system = models.CharField('System', max_length=255, blank=True, null=True)
    device_utility = models.CharField('Utility', max_length=255, blank=True, null=True)
    device_HDD = models.CharField('HDD', max_length=255, blank=True, null=True)
    device_IP_rj45 = models.CharField('IP Rj45', max_length=255, blank=True, null=True)
    device_MAC_rj45 = models.CharField('MAC Rj45', max_length=255, blank=True, null=True)
    device_IP_wifi = models.CharField('IP WiFi', max_length=255, blank=True, null=True)
    device_MAC_wifi = models.CharField('MAC WiFi', max_length=255, blank=True, null=True)
    device_RAM = models.CharField('RAM', max_length=255, blank=True, null=True)
    device_SSD = models.CharField('SSD', max_length=255, blank=True, null=True)

    # https://www.youtube.com/watch?v=_ph8GF84fX4
    device_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', blank=True, null=True)
    # https://www.youtube.com/watch?v=jFqYuWNyLnI
    device_category = models.ForeignKey(DeviceCategory, on_delete=models.CASCADE, verbose_name='Category', blank=True, null=True)

    device_favorite = models.BooleanField('Favorite', default='False')
    device_status = models.CharField('Status', max_length=12, choices=options, default='private')

    # https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models

    # Metadata
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        ordering = ('device_brand', )

    # Methods
    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('device-detail', args=[str(self.id)])

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets dans la base de données."""
        return self.device_brand

### Fin
