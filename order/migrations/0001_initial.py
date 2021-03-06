# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Invoice'
        db.create_table(u'order_invoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice_num', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('payment_method', self.gf('django.db.models.fields.CharField')(default='PP', max_length=2)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('payer', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('when_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('when_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('coupon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Coupon'], null=True, blank=True)),
            ('subtotal', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('tax', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('delivery', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('discount', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('customer_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=256)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='invoices', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'order', ['Invoice'])

        # Adding model 'DeliveryWindow'
        db.create_table(u'order_deliverywindow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(related_name='delivery_windows', to=orm['shop.Store'])),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'order', ['DeliveryWindow'])

        # Adding model 'OrderItem'
        db.create_table(u'order_orderitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Order'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Item'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('allow_sub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('item_cost', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('item_tax', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
        ))
        db.send_create_signal(u'order', ['OrderItem'])

        # Adding model 'Order'
        db.create_table(u'order_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subtotal', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('tax', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('delivery_window', self.gf('django.db.models.fields.related.ForeignKey')(related_name='orders', on_delete=models.PROTECT, to=orm['order.DeliveryWindow'])),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(related_name='orders', on_delete=models.PROTECT, to=orm['order.Invoice'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('when_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('when_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'order', ['Order'])

        # Adding model 'Coupon'
        db.create_table(u'order_coupon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('expire', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(9999, 12, 31, 0, 0), blank=True)),
        ))
        db.send_create_signal(u'order', ['Coupon'])


    def backwards(self, orm):
        # Deleting model 'Invoice'
        db.delete_table(u'order_invoice')

        # Deleting model 'DeliveryWindow'
        db.delete_table(u'order_deliverywindow')

        # Deleting model 'OrderItem'
        db.delete_table(u'order_orderitem')

        # Deleting model 'Order'
        db.delete_table(u'order_order')

        # Deleting model 'Coupon'
        db.delete_table(u'order_coupon')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'order.coupon': {
            'Meta': {'object_name': 'Coupon'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'expire': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(9999, 12, 31, 0, 0)', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'})
        },
        u'order.deliverywindow': {
            'Meta': {'object_name': 'DeliveryWindow'},
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'delivery_windows'", 'to': u"orm['shop.Store']"})
        },
        u'order.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'coupon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order.Coupon']", 'null': 'True', 'blank': 'True'}),
            'customer_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'delivery': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_num': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'payer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'default': "'PP'", 'max_length': '2'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'subtotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invoices'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'when_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'when_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'order.order': {
            'Meta': {'object_name': 'Order'},
            'delivery_window': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'on_delete': 'models.PROTECT', 'to': u"orm['order.DeliveryWindow']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'on_delete': 'models.PROTECT', 'to': u"orm['order.Invoice']"}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'orders'", 'symmetrical': 'False', 'through': u"orm['order.OrderItem']", 'to': u"orm['shop.Item']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'subtotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'when_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'when_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'order.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            'allow_sub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Item']"}),
            'item_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'item_tax': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order.Order']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shop.category': {
            'Meta': {'object_name': 'Category'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sub_categories'", 'null': 'True', 'to': u"orm['shop.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'on_delete': 'models.PROTECT', 'to': u"orm['shop.Store']"})
        },
        u'shop.item': {
            'Meta': {'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'on_delete': 'models.PROTECT', 'to': u"orm['shop.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_quantity_per_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'on_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'out_of_stock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'sales_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sold_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tax_class': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '3', 'decimal_places': '2'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'when_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'shop.store': {
            'Meta': {'object_name': 'Store'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['order']
