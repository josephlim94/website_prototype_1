from django.contrib import admin

# Register your models here.
from .models import ListingData, ListingUserGroup

admin.site.register(ListingData)
admin.site.register(ListingUserGroup)