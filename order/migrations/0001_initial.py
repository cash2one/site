# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Cart'
        db.create_table(u'order_cart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_checked_out', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'order', ['Cart'])

        # Adding model 'CartItem'
        db.create_table(u'order_cartitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Cart'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'order', ['CartItem'])

        # Adding model 'OrderStatus'
        db.create_table(u'order_orderstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_initial', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_closing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('index_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'order', ['OrderStatus'])

        # Adding model 'Order'
        db.create_table(u'order_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('delivery_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('payment_type', self.gf('django.db.models.fields.CharField')(default='cash_payment', max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status',
             self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.OrderStatus'], null=True, blank=True)),
        ))
        db.send_create_signal(u'order', ['Order'])

        # Adding model 'OrderItem'
        db.create_table(u'order_orderitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Order'])),
            ('passport',
             self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressprogram.AdvertisingSpace'], null=True,
                                                                   on_delete=models.SET_NULL)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=0)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'order', ['OrderItem'])

        # Adding model 'OrderOneClick'
        db.create_table(u'order_orderoneclick', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'order', ['OrderOneClick'])

        # Adding model 'OrderOneClickItem'
        db.create_table(u'order_orderoneclickitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_one_click', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.OrderOneClick'])),
            ('product',
             self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressprogram.AdvertisingSpace'], null=True,
                                                                   on_delete=models.SET_NULL)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=0)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'order', ['OrderOneClickItem'])

    def backwards(self, orm):
        # Deleting model 'Cart'
        db.delete_table(u'order_cart')

        # Deleting model 'CartItem'
        db.delete_table(u'order_cartitem')

        # Deleting model 'OrderStatus'
        db.delete_table(u'order_orderstatus')

        # Deleting model 'Order'
        db.delete_table(u'order_order')

        # Deleting model 'OrderItem'
        db.delete_table(u'order_orderitem')

        # Deleting model 'OrderOneClick'
        db.delete_table(u'order_orderoneclick')

        # Deleting model 'OrderOneClickItem'
        db.delete_table(u'order_orderoneclickitem')

    models = {
        u'addressprogram.advertisingspace': {
            'Meta': {'ordering': "('address__address', 'side')", 'object_name': 'AdvertisingSpace'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.GeoObject']"}),
            'backlight': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '5'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 1, 13, 0, 0)'}),
            'description': (
            'django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
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
            'based': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 1, 13, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'distance': (
            'django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'emblem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'population': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.Region']"}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'transport': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'addressprogram.construction': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Construction'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 1, 13, 0, 0)'}),
            'icon': ('django.db.models.fields.files.ImageField', [],
                     {'default': "'/media/images/logo.png'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'short_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_city': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_main': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'addressprogram.geoobject': {
            'Meta': {'ordering': "('address',)", 'object_name': 'GeoObject'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.City']"}),
            'construction': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 1, 13, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'prod': ('django.db.models.fields.related.ForeignKey', [],
                     {'default': '1', 'to': u"orm['addressprogram.Construction']"})
        },
        u'addressprogram.region': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Region'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 1, 13, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType', 'db_table': "'django_content_type'"},
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
            'content_type': (
            'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'order.order': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'Order'},
            'address': (
            'django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delivery_type': (
            'django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_type': (
            'django.db.models.fields.CharField', [], {'default': "'cash_payment'", 'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'postal_code': (
            'django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['order.OrderStatus']", 'null': 'True', 'blank': 'True'})
        },
        u'order.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order.Order']"}),
            'passport': ('django.db.models.fields.related.ForeignKey', [],
                         {'to': u"orm['addressprogram.AdvertisingSpace']", 'null': 'True',
                          'on_delete': 'models.SET_NULL'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '2'}),
            'product_name': (
            'django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '0'})
        },
        u'order.orderoneclick': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'OrderOneClick'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'order.orderoneclickitem': {
            'Meta': {'object_name': 'OrderOneClickItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_one_click': (
            'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order.OrderOneClick']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [],
                        {'to': u"orm['addressprogram.AdvertisingSpace']", 'null': 'True',
                         'on_delete': 'models.SET_NULL'}),
            'product_name': (
            'django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '0'})
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
