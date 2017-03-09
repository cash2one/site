# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Deleting model 'OrderOneClickItem'
        db.delete_table(u'order_orderoneclickitem')

        # Deleting model 'OrderOneClick'
        db.delete_table(u'order_orderoneclick')

        # Deleting field 'Order.comment'
        db.delete_column(u'order_order', 'comment')

        # Deleting field 'Order.delivery_type'
        db.delete_column(u'order_order', 'delivery_type')

        # Deleting field 'Order.postal_code'
        db.delete_column(u'order_order', 'postal_code')

        # Deleting field 'Order.address'
        db.delete_column(u'order_order', 'address')

        # Deleting field 'Order.city'
        db.delete_column(u'order_order', 'city')

        # Deleting field 'Order.payment_type'
        db.delete_column(u'order_order', 'payment_type')

        # Adding field 'Order.company'
        db.add_column(u'order_order', 'company',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Order.date_start'
        db.add_column(u'order_order', 'date_start',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Order.date_end'
        db.add_column(u'order_order', 'date_end',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Changing field 'Order.created_at'
        db.alter_column(u'order_order', 'created_at',
                        self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

        # Changing field 'Order.email'
        db.alter_column(u'order_order', 'email',
                        self.gf('django.db.models.fields.EmailField')(default='', max_length=75))
        # Deleting field 'OrderItem.price'
        db.delete_column(u'order_orderitem', 'price')

        # Deleting field 'OrderItem.product_name'
        db.delete_column(u'order_orderitem', 'product_name')

        # Adding field 'OrderItem.grp'
        db.add_column(u'order_orderitem', 'grp',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'OrderItem.ots'
        db.add_column(u'order_orderitem', 'ots',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'OrderItem.passport_name'
        db.add_column(u'order_orderitem', 'passport_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Adding model 'OrderOneClickItem'
        db.create_table(u'order_orderoneclickitem', (
            ('product',
             self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressprogram.AdvertisingSpace'], null=True,
                                                                   on_delete=models.SET_NULL)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=2)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_one_click', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.OrderOneClick'])),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=0)),
        ))
        db.send_create_signal(u'order', ['OrderOneClickItem'])

        # Adding model 'OrderOneClick'
        db.create_table(u'order_orderoneclick', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'order', ['OrderOneClick'])

        # Adding field 'Order.comment'
        db.add_column(u'order_order', 'comment',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Order.delivery_type'
        db.add_column(u'order_order', 'delivery_type',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Order.postal_code'
        db.add_column(u'order_order', 'postal_code',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Order.address'
        db.add_column(u'order_order', 'address',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Order.city'
        db.add_column(u'order_order', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Order.payment_type'
        db.add_column(u'order_order', 'payment_type',
                      self.gf('django.db.models.fields.CharField')(default='cash_payment', max_length=255),
                      keep_default=False)

        # Deleting field 'Order.company'
        db.delete_column(u'order_order', 'company')

        # Deleting field 'Order.date_start'
        db.delete_column(u'order_order', 'date_start')

        # Deleting field 'Order.date_end'
        db.delete_column(u'order_order', 'date_end')

        # User chose to not deal with backwards NULL issues for 'Order.created_at'
        raise RuntimeError("Cannot reverse this migration. 'Order.created_at' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Order.created_at'
        db.alter_column(u'order_order', 'created_at',
                        self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Order.email'
        db.alter_column(u'order_order', 'email',
                        self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))

        # User chose to not deal with backwards NULL issues for 'OrderItem.price'
        raise RuntimeError("Cannot reverse this migration. 'OrderItem.price' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct migration        # Adding field 'OrderItem.price'
        db.add_column(u'order_orderitem', 'price',
                      self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=2),
                      keep_default=False)

        # Adding field 'OrderItem.product_name'
        db.add_column(u'order_orderitem', 'product_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'OrderItem.grp'
        db.delete_column(u'order_orderitem', 'grp')

        # Deleting field 'OrderItem.ots'
        db.delete_column(u'order_orderitem', 'ots')

        # Deleting field 'OrderItem.passport_name'
        db.delete_column(u'order_orderitem', 'passport_name')

    models = {
        u'addressprogram.advertisingspace': {
            'Meta': {'ordering': "('address__address', 'side')", 'object_name': 'AdvertisingSpace'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.GeoObject']"}),
            'backlight': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '5'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 1, 26, 0, 0)'}),
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
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 1, 26, 0, 0)'}),
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
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'transport': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'addressprogram.construction': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Construction'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 1, 26, 0, 0)'}),
            'icon': ('django.db.models.fields.files.ImageField', [],
                     {'default': "'/media/images/logo.png'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker_icon': ('django.db.models.fields.files.ImageField', [],
                            {'default': "'/media/images/type1.png'", 'max_length': '100'}),
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
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 1, 26, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'prod': ('django.db.models.fields.related.ForeignKey', [],
                     {'default': '1', 'to': u"orm['addressprogram.Construction']"})
        },
        u'addressprogram.region': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Region'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 1, 26, 0, 0)'}),
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
            'grp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ots': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'order.order': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'Order'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'created_at': (
            'django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['order.OrderStatus']", 'null': 'True', 'blank': 'True'})
        },
        u'order.orderitem': {
            'Meta': {'ordering': "('order',)", 'object_name': 'OrderItem'},
            'grp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order.Order']"}),
            'ots': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'passport': ('django.db.models.fields.related.ForeignKey', [],
                         {'to': u"orm['addressprogram.AdvertisingSpace']", 'null': 'True',
                          'on_delete': 'models.SET_NULL'}),
            'passport_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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
