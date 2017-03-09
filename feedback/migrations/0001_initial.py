# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Feedback'
        db.create_table(u'feedback_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'feedback', ['Feedback'])

    def backwards(self, orm):
        # Deleting model 'Feedback'
        db.delete_table(u'feedback_feedback')

    models = {
        u'feedback.feedback': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'Feedback'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['feedback']
