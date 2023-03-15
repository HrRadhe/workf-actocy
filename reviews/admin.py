from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('order', 'heading', 'star', 'user', 'serviceman','created_at')

admin.site.register(Review, ReviewAdmin)