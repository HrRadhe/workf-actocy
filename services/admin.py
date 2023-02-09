from django.contrib import admin
from .models import MainService, SubService

# Register your models here
class MainServiceAdmin(admin.ModelAdmin):
    list_display =('serviceman', 'user', 'name')

class SubServiceAdmin(admin.ModelAdmin):
    list_display =('serviceman', 'user', 'name')

admin.site.register(MainService, MainServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)
# Register your models here.
