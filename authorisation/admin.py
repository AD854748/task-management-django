
import logging
from django.contrib import admin
from import_export import resources
from authorisation.models import CustomUser
from myproject.admin import admin_site
from import_export.admin import ImportExportMixin
from simple_history.admin import SimpleHistoryAdmin


logger = logging.getLogger(__name__)

# Register your models here.

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomUserResource, self).__init__(*args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        if not instance.created_by:
            instance.created_by = self.request.user.username
        instance.last_updated_by = self.request.user.username
        return super().before_save_instance(instance, using_transactions, dry_run)

@admin.register(CustomUser, site=admin_site)
class CustomUserAdmin(ImportExportMixin, SimpleHistoryAdmin):
    resource_class = CustomUserResource
    list_display = ('id', 'email','first_name', 'last_name')
  

    def get_resource_kwargs(self, request, *args, **kwargs):
        return {'request' : request}


