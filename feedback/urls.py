# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('feedback.views',
                       # url(r'^kontakty/$', 'render_contacts', name='contacts'),
    url(r'^feedback_form/$', 'process_feedback_form', name='process-feedback'),
                       url(r'^feedback_manager/$', 'process_feedback_manager', name='feedback-manager'),
                       )