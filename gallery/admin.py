from django.contrib import admin
from .models import UserProfile, Images


class UserProfileAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email')

class ImagesAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'uploaded_at', 'modified_at')



admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Images, ImagesAdmin)