from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
from django.contrib.auth.models import User

from accounts.models import BlogUser


class BlogUserInline(admin.StackedInline):
    model = BlogUser
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (BlogUserInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(BlogUser)