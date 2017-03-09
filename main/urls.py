# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^$', TemplateView.as_view(template_name='index.html')),
                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^dismiss_snc/$',
                       #     'main.views.close_special_modal',
                       #     name="dismiss-snc"),
                       url(r'^', include('announce.urls', namespace='announce')),
                       url(r'^', include('news.urls', namespace='news')),
                       url(r'^', include('services.urls', namespace='services')),
                       url(r'^', include('addressprogram.urls', namespace='program')),
                       url(r'^', include('order.urls', namespace='order')),
                       )

if 'tinymce' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
                            url(r'^tinymce/', include('tinymce.urls')),
                            )

if 'filebrowser' in settings.INSTALLED_APPS:
    from filebrowser.sites import site

    urlpatterns += patterns('',
                            url(r'^admin/filebrowser/', include(site.urls)),
                            )

if 'grappelli' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
                            url(r'^grappelli/', include('grappelli.urls')),
                            )

if 'registration' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
                            url(r'^accounts/', include('accounts.urls')),
                            )

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }),
                            )

urlpatterns += patterns('main.views',
                        url(r'^change_theme/$', 'change_theme', name='change-theme'),
                        )

urlpatterns += patterns('',
                        url(r'^sitemap.xml$', 'simplesitemap.views.sitemap_gen', ),
                        url(r'^robots\.txt$',
                            TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
                        )

if 'constance' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
                            url(r'^admin/constance/config/', 'constance.views.ChangeList'),
                            )

urlpatterns += patterns('',
                        url(r'^', include('mapelements.urls', namespace='mapelements')),
                        url(r'^', include('feedback.urls', namespace='feedback')),
                        url(r'^', include('flatpages.urls', namespace='fpc')),
                        )
