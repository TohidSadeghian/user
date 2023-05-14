from django.contrib import admin
from .models import UserModels
from django.contrib.auth.admin import UserAdmin


@admin.register(UserModels)
class UserAdmin(UserAdmin):

      fieldsets = ((('User'),{'fields':('user_id','password')}),
      (('personal_info'),{'fields':('first_name','last_name','email')}),
      (('permissions'),{'fields':('is_active', 'is_staff', 'is_superuser','groups',
                   'user_permissions')}),
      (('Important dates'),{'fields':('last_login', 'date_joined')}))
      list_display=['user_id', 'username']
      search_fields=['user_id']
      list_per_page=10

