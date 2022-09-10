from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin

from .models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)
    fields = ('image', 'get_preview', 'number')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
