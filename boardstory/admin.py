from django.contrib import admin
from .models import StoryModel

class StoryModelAdmin(admin.ModelAdmin):
    list_display = ('status','title','description','last_updated_on','is_visible','assigned_to','assignee','priority')  # Display all fields

admin.site.register(StoryModel, StoryModelAdmin)



  






