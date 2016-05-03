from django.contrib import admin
from search.models import SearchQuery,AppInfo
# Register your models here.


class SearchQueryFormAdmin(admin.ModelAdmin):
	pre_fields={'slug':('query',)}

admin.site.register(SearchQuery,SearchQueryFormAdmin)
admin.site.register(AppInfo)