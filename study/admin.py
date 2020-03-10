from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Test
from .models import Quest
from .models import Answer
from .models import School
from .models import Useranswer
from .models import User#,UserManager

#class UserAdmin(BaseUserAdmin):
   # form = UserAdminChangeForm
   # add_form = UserAdminCreationForm
   # list_display = ('email', 'admin')
    #list_filter = ('admin',)
    #fieldsets = (
     #   (None, {'fields': ('email', 'password')}),
      #  ('Personal info', {'fields': ()}),
       # ('Permissions', {'fields': ('admin',)}),
    #)
    #add_fieldsets = (
     #   (None, {
      #      'classes': ('wide',),
       #     'fields': ('email', 'password1', 'password2')}
       # ),
   # )
    #search_fields = ('email',)
    #ordering = ('email',)
    #filter_horizontal = ()


admin.site.register(User)#,UserManager)
admin.site.register(Test)
admin.site.register(Quest)
admin.site.register(Answer)
admin.site.register(School)
admin.site.register(Useranswer)
