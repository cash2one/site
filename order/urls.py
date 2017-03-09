# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('order.views',
                       url(r'^order/$', 'get_cart', name='get-cart'),
                       url(r'^remove/(?P<item_id>\d+)/$', 'remove_from_cart', name='remove_from_cart'),
                       url(r'^clear_card/$', 'clear_cart', name='clear_cart'),
                       url(r'^order/checkout/$', 'checkout', name='checkout'),
                       url(r'^order_exel/$', 'download_order_exel', name='order_exel'),
                       )
