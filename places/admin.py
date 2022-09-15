from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    list_display = ('image', 'image_id')
    fields = ('number', 'image', 'get_preview')
    readonly_fields = ('get_preview',)
    ordering = ('number', )

    def get_preview(self, object):
        if object.image:
            return format_html(f'<img src="{object.image.url}" height="200px" />')

    get_preview.short_description = 'Превью'

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
