from django.contrib import admin
from .models import User
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('email','phone_number','first_name','last_name','username','role','is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'pin_code', 'created_at')

admin.site.register(User,CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


