from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *
# Register your models here.


class AdminCustomuser(UserAdmin):

     form = UserChangeForm
     add_form = CustomUserForm


     list_display = ('mobile_number','email','name','family','gender','is_active','is_admin',)
     list_filter= ('is_active','is_admin')
     search_fields = ('mobile_number','is_active','gender',)
     ordering = ('is_active','gender')


     fieldsets = (
            (None,{'fields':('mobile_number','password',)}),
            ('Personal Info',{'fields':('email','name','family','gender','active_code',)}),
             ('Permissions', {'fields': ('is_active', 'is_admin','is_superuser', 'groups', 'user_permissions')}),
            )


     add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('mobile_number', 'password', 're_password', 'name', 'family', 'gender'),
    }),
)



     search_fields = ('mobile_number',)
     ordering = ('mobile_number',)
     filter_horizontal = ('groups','user_permissions',)


admin.site.register(Customuser,AdminCustomuser)


