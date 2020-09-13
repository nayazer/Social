from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
  list_display = ('id','title','is_published','date')
  list_display_links = ('title',)
  list_filter = ('title',)
  list_editable = ('is_published',)
  search_fields = ('title','description')
  list_per_page = 25

admin.site.register(Service, ServiceAdmin)