from django.contrib import admin

# Register your models here.
from .models import WorldBorder, Profile, CountryInfo

admin.site.register(WorldBorder, admin.ModelAdmin)
admin.site.register(Profile, admin.ModelAdmin)
admin.site.register(CountryInfo, admin.ModelAdmin)
