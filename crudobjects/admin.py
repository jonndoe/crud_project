from django.contrib import admin

from .models import Crudobject



class CrudobjectAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price",)



admin.site.register(Crudobject, CrudobjectAdmin)