from django.contrib import admin

from .models import Image, Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ("place", "order")
    pass
