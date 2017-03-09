# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'OrderItem.quantity'
        db.alter_column(u'order_orderitem', 'quantity', self.gf('django.db.models.fields.SmallIntegerField')())
        # Adding field 'Order.ip'
        db.add_column(u'order_order', 'ip',
                      self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'OrderItem.quantity'
        db.alter_column(u'order_orderitem', 'quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=0))
        # Deleting field 'Order.ip'
        db.delete_column(u'order_order', 'ip')


    models = {
        u'addressprogram.advertisingspace': {
            'Meta': {'ordering': "('address__address', 'side')", 'object_name': 'AdvertisingSpace'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.GeoObject']"}),
            'backlight': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '5'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 2, 14, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'has_print': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'material': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ots': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'scheme': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.Construction']"})
        },
        u'addressprogram.city': {
            'Meta': {'ordering': "('order',)", 'object_name': 'City'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'available_constructions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['addressprogram.Construction']", 'symmetrical': 'False', 'blank': 'True'}),
            'based': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 2, 14, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'emblem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'population': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.Region']"}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'transport': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'addressprogram.construction': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Construction'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 2, 14, 0, 0)'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/images/logo.png'", 'max_length': '100'}),
            'icon_active': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/images/logo.png'", 'max_length': '100'}),
            'icon_hover': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/images/logo.png'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker_icon': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/images/type1.png'", 'max_length': '100'}),
            'marker_icon_active': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/images/type1-active.png'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'short_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_footer': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_city': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_main': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'addressprogram.geoobject': {
            'Meta': {'ordering': "('address',)", 'object_name': 'GeoObject'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.City']"}),
            'construction': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 2, 14, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'prod': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['addressprogram.Construction']"})
        },
        u'addressprogram.region': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Region'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 2, 14, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'order.cart': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'Cart'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_checked_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'order.cartitem': {
            'Meta': {'ordering': "('cart',)", 'object_name': 'CartItem'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order.Cart']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'grp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ots': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'order.order': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'Order'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order.OrderStatus']", 'null': 'True', 'blank': 'True'})
        },
        u'order.orderitem': {
            'Meta': {'ordering': "('order',)", 'object_name': 'OrderItem'},
            'grp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order.Order']"}),
            'ots': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'passport': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.AdvertisingSpace']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'passport_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'})
        },
        u'order.orderstatus': {
            'Meta': {'object_name': 'OrderStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_closing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_initial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['order']