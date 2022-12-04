from django.contrib import admin
from apps.main.models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


class FlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


admin.site.unregister(FlatPage)
admin.site.register(AboutUs)
admin.site.register(OurBlog)
admin.site.register(FlatPage, FlatPageAdmin)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('admin_phone', 'updated_at', 'created_at')
    list_editable = ('admin_phone',)
    list_display_links = None


@admin.register(FormWholesaler)
class FormWholesalerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'business_type', 'created_at')
    list_display_links = ('name', 'phone')
