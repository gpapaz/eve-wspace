# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MapSystem.display_order_priority'
        db.add_column(u'Map_mapsystem', 'display_order_priority',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MapSystem.display_order_priority'
        db.delete_column(u'Map_mapsystem', 'display_order_priority')


    models = {
        u'Map.destination': {
            'Meta': {'object_name': 'Destination'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destinations'", 'to': u"orm['Map.KSystem']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destinations'", 'null': 'True', 'to': u"orm['account.EWSUser']"})
        },
        u'Map.ksystem': {
            'Meta': {'object_name': 'KSystem', '_ormbases': [u'Map.System']},
            'jumps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sov': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'system_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['Map.System']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'Map.map': {
            'Meta': {'object_name': 'Map'},
            'explicitperms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'root': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'root'", 'to': u"orm['Map.System']"}),
            'truncate_allowed': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'Map.maplog': {
            'Meta': {'object_name': 'MapLog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'logentries'", 'to': u"orm['Map.Map']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'maplogs'", 'to': u"orm['account.EWSUser']"}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'Map.mappermission': {
            'Meta': {'object_name': 'MapPermission'},
            'access': ('django.db.models.fields.IntegerField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mappermissions'", 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'grouppermissions'", 'to': u"orm['Map.Map']"})
        },
        u'Map.mapsystem': {
            'Meta': {'object_name': 'MapSystem'},
            'display_order_priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'friendlyname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interesttime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'systems'", 'to': u"orm['Map.Map']"}),
            'parentsystem': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'childsystems'", 'null': 'True', 'to': u"orm['Map.MapSystem']"}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'maps'", 'to': u"orm['Map.System']"})
        },
        u'Map.signature': {
            'Meta': {'ordering': "['sigid']", 'unique_together': "(('system', 'sigid'),)", 'object_name': 'Signature'},
            'activated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'downtimes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '65', 'null': 'True', 'blank': 'True'}),
            'lastescalated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'signatures'", 'null': 'True', 'to': u"orm['account.EWSUser']"}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'owned_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sigs_owned'", 'null': 'True', 'to': u"orm['account.EWSUser']"}),
            'owned_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'ratscleared': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sigid': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sigtype': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sigs'", 'null': 'True', 'to': u"orm['Map.SignatureType']"}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'signatures'", 'to': u"orm['Map.System']"}),
            'updated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'Map.signaturetype': {
            'Meta': {'object_name': 'SignatureType'},
            'escalatable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'longname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'sleeprsite': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'Map.sitespawn': {
            'Meta': {'object_name': 'SiteSpawn'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sigtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Map.SignatureType']"}),
            'sitename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'spawns': ('django.db.models.fields.TextField', [], {}),
            'sysclass': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Map.snapshot': {
            'Meta': {'object_name': 'Snapshot'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'snapshots'", 'to': u"orm['account.EWSUser']"})
        },
        u'Map.system': {
            'Meta': {'object_name': 'System', '_ormbases': [u'core.SystemData']},
            'first_visited': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'last_visited': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'lastscanned': ('django.db.models.fields.DateTimeField', [], {}),
            'npckills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'occupied': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'podkills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shipkills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sysclass': ('django.db.models.fields.IntegerField', [], {}),
            u'systemdata_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.SystemData']", 'unique': 'True', 'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'Map.wormhole': {
            'Meta': {'object_name': 'Wormhole'},
            'bottom': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'parent_wormhole'", 'unique': 'True', 'null': 'True', 'to': u"orm['Map.MapSystem']"}),
            'bottom_bubbled': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bottom_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['Map.WormholeType']"}),
            'collapsed': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'eol_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wormholes'", 'to': u"orm['Map.Map']"}),
            'mass_status': ('django.db.models.fields.IntegerField', [], {}),
            'time_status': ('django.db.models.fields.IntegerField', [], {}),
            'top': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'child_wormholes'", 'to': u"orm['Map.MapSystem']"}),
            'top_bubbled': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'top_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['Map.WormholeType']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'Map.wormholetype': {
            'Meta': {'object_name': 'WormholeType'},
            'destination': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jumpmass': ('django.db.models.fields.BigIntegerField', [], {}),
            'lifetime': ('django.db.models.fields.IntegerField', [], {}),
            'maxmass': ('django.db.models.fields.BigIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'Map.wsystem': {
            'Meta': {'object_name': 'WSystem', '_ormbases': [u'Map.System']},
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'is_shattered': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'static1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'primary_statics'", 'null': 'True', 'to': u"orm['Map.WormholeType']"}),
            'static2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'secondary_statics'", 'null': 'True', 'to': u"orm['Map.WormholeType']"}),
            u'system_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['Map.System']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'account.ewsuser': {
            'Meta': {'object_name': 'EWSUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'defaultmap': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'defaultusers'", 'null': 'True', 'to': u"orm['Map.Map']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.constellation': {
            'Meta': {'object_name': 'Constellation', 'db_table': "'mapConstellations'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'constellationID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'constellationName'"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constellations'", 'db_column': "'regionID'", 'to': u"orm['core.Region']"}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {}),
            'z': ('django.db.models.fields.FloatField', [], {})
        },
        u'core.region': {
            'Meta': {'object_name': 'Region', 'db_table': "'mapRegions'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'regionID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'regionName'"}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {}),
            'z': ('django.db.models.fields.FloatField', [], {})
        },
        u'core.systemdata': {
            'Meta': {'object_name': 'SystemData', 'db_table': "'mapSolarSystems'", 'managed': 'False'},
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'systems'", 'db_column': "'constellationID'", 'to': u"orm['core.Constellation']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'solarSystemID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'solarSystemName'"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'systems'", 'db_column': "'regionID'", 'to': u"orm['core.Region']"}),
            'security': ('django.db.models.fields.FloatField', [], {}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {}),
            'z': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['Map']