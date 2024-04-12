
from django.contrib.admin import AdminSite
from django.contrib import admin
from django.contrib.auth.models import Group, User, Permission
from authorisation.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from boardstory.models import StoryModel
admin.site.register(CustomUser)

class MyAdminSite(AdminSite):
    site_header = 'Myproject - Admin'

    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()
        return urls

admin_site = MyAdminSite(name='myproject')

@admin.register(Group, site=admin_site)
class GroupAdmin(admin.ModelAdmin):
    class Meta:
        model = Group
        fields = ('__all__')

@admin.register(User, site=admin_site)
class UserAdmin(UserAdmin):
    class Meta:
        model = User
        fields = ('__all__')

@admin.register(Permission, site=admin_site)
class PermissionAdmin(admin.ModelAdmin):
    class Meta:
        model = Permission
        fields = ('__all__')
