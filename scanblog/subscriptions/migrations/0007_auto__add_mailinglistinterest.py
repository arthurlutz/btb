# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MailingListInterest'
        db.create_table(u'subscriptions_mailinglistinterest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('volunteering', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allies', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('announcements', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('details', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'subscriptions', ['MailingListInterest'])


    def backwards(self, orm):
        # Deleting model 'MailingListInterest'
        db.delete_table(u'subscriptions_mailinglistinterest')


    models = {
        u'annotations.replycode': {
            'Meta': {'object_name': 'ReplyCode'},
            'code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '16', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'annotations.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'post_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
        u'campaigns.campaign': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Campaign'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'ended': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profiles.Organization']", 'symmetrical': 'False'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reply_code': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['annotations.ReplyCode']", 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'comments.comment': {
            'Meta': {'ordering': "['created']", 'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'comment_doc': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['scanning.Document']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comments'", 'null': 'True', 'to': u"orm['scanning.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.affiliation': {
            'Meta': {'ordering': "['order', '-created']", 'object_name': 'Affiliation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'detail_body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_body': ('django.db.models.fields.TextField', [], {}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profiles.Organization']", 'symmetrical': 'False'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'profiles.organization': {
            'Meta': {'object_name': 'Organization'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'custom_intro_packet': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'footer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing_address': ('django.db.models.fields.TextField', [], {}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'moderators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'organizations_moderated'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'outgoing_mail_handled_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.Organization']", 'null': 'True', 'blank': 'True'}),
            'personal_contact': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'scanning.document': {
            'Meta': {'ordering': "['-date_written']", 'object_name': 'Document'},
            'adult': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'affiliation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.Affiliation']", 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents_authored'", 'to': u"orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_written': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents_edited'", 'to': u"orm['auth.User']"}),
            'highlight': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'highlight_transform': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_reply_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'document_replies'", 'null': 'True', 'to': u"orm['annotations.ReplyCode']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'reply_code': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['annotations.ReplyCode']", 'unique': 'True'}),
            'scan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scanning.Scan']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '20', 'db_index': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['annotations.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'under_construction': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'scanning.scan': {
            'Meta': {'ordering': "['created']", 'object_name': 'Scan'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scans_authored'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'org': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.Organization']", 'null': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'processing_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'under_construction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uploader': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scans_uploaded'", 'to': u"orm['auth.User']"})
        },
        u'subscriptions.commentnotificationlog': {
            'Meta': {'object_name': 'CommentNotificationLog'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comments.Comment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'subscriptions.documentnotificationlog': {
            'Meta': {'object_name': 'DocumentNotificationLog'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scanning.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'subscriptions.mailinglistinterest': {
            'Meta': {'object_name': 'MailingListInterest'},
            'allies': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'announcements': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'volunteering': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'subscriptions.notificationblacklist': {
            'Meta': {'object_name': 'NotificationBlacklist'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'subscriptions.subscription': {
            'Meta': {'ordering': "['tag', 'author', 'document', 'campaign', 'affiliation']", 'object_name': 'Subscription'},
            'affiliation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'affiliation_subscriptions'", 'null': 'True', 'to': u"orm['profiles.Affiliation']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'author_subscriptions'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'organization_subscriptions'", 'null': 'True', 'to': u"orm['campaigns.Campaign']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subscriptions'", 'null': 'True', 'to': u"orm['scanning.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'organization_subscriptions'", 'null': 'True', 'to': u"orm['profiles.Organization']"}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subscriptions'", 'to': u"orm['auth.User']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tag_subscriptions'", 'null': 'True', 'to': u"orm['annotations.Tag']"})
        },
        u'subscriptions.usernotificationlog': {
            'Meta': {'ordering': "['-date']", 'object_name': 'UserNotificationLog'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['subscriptions']