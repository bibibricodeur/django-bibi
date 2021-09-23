from django.contrib import admin

from device.models import DevicePost, DeviceCategory

# Register your models here.

@admin.register(DevicePost)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_brand', 'device_model', 'device_utility')
    #list_filter = ()
    #search_fields = ()
    pass
    #list_display = ()

@admin.register(DeviceCategory)
class DeviceCategoryAdmin(admin.ModelAdmin):
    #pass
    list_display = ('category_name', )
