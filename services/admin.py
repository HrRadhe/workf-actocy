from django.contrib import admin
from .models import MainService, SubService,ServicesImage

# Register your models here
class MainServiceAdmin(admin.ModelAdmin):
    list_display =('serviceman', 'user', 'name')

class SubServiceAdmin(admin.ModelAdmin):
    list_display =('serviceman', 'user', 'name')

class ServiceImageAdmin(admin.ModelAdmin):
    list_display =('pk', 'service', 'service_img')

admin.site.register(MainService, MainServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)
admin.site.register(ServicesImage, ServiceImageAdmin)
# Register your models here.
