from django.contrib import admin

from .models import *
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick_name', 'birday', 'gender']


# admin.site.register(UserProfile, UserProfileAdmin)