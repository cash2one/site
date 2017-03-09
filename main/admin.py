# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.sites.models import Site

from .models import RobotsSettings, YaSettings,MetaSettings, DefaultSettings


class RobotsSettingsInline(admin.StackedInline):
    model = RobotsSettings
    can_delete = False
    extra = 1


class MetricaSettingsInline(admin.StackedInline):
    model = YaSettings
    can_delete = False
    extra = 1


class MetaSettingsInline(admin.StackedInline):
    model = MetaSettings
    can_delete = False
    extra = 1


class SEOSettingsInline(admin.StackedInline):
    model = DefaultSettings
    can_delete = False
    extra = 1


class SiteAdmin(admin.ModelAdmin):
    inlines = [
        RobotsSettingsInline,MetricaSettingsInline,MetaSettingsInline,SEOSettingsInline,
    ]
    list_display = ('name', 'domain')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(SiteAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


def site_unicode(self):
    return self.name
Site.__unicode__ = site_unicode
Site._meta.ordering = ['name',]


admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)