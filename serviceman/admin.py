from django.contrib import admin
from .models import Serviceman

# Register your models here.
class serviceAdmin(admin.ModelAdmin):
    list_display =('user','is_approved','created_at','serviceman_slug')
    list_display_links = ('user','serviceman_slug',)
    list_editable = ('is_approved',)


admin.site.register(Serviceman, serviceAdmin)
