from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# class CustomAdminUSer(UserAdmin):
#     list_display=['username','user_types']
admin.site.register(CustomUser)