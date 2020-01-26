from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Accident)
admin.site.register(models.QueryItem)