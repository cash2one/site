# -*- coding: utf-8 -*-

from django.contrib.contenttypes import generic
from simplesitemap.models import BasicSitemapData


class SitemapFormset(generic.BaseGenericInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super(SitemapFormset, self)._construct_form(i, **kwargs)

        form.empty_permitted = False
        form.has_changed = lambda: True

        if self.instance:
            self.instance.__sitemap_metadata_handled = True

        return form


def map_inline():
    attrs = {
        'max_num': 1,
        'extra': 1,
        'model': BasicSitemapData,
        'ct_field': "item_model",
        'ct_fk_field': "item_id",
        'formset': SitemapFormset,
        }
    return type('SitemapdataInline', (generic.GenericStackedInline,), attrs)
