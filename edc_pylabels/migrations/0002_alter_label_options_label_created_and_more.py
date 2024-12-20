# Generated by Django 5.1.2 on 2024-11-03 17:09

import _socket
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_pylabels", "0003_rename_updated_labelspecification_modified"),
        ("edc_pylabels", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="label",
            options={
                "default_manager_name": "objects",
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
                "verbose_name": "Label",
                "verbose_name_plural": "Labels",
            },
        ),
        migrations.AddField(
            model_name="label",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AddField(
            model_name="label",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AddField(
            model_name="label",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="revision",
            field=django_revision.revision_field.RevisionField(
                blank=True,
                editable=False,
                help_text="System field. Git repository tag:branch:commit.",
                max_length=75,
                null=True,
                verbose_name="Revision",
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AddField(
            model_name="label",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="label",
            name="id",
            field=django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                blank=True,
                editable=False,
                help_text="System auto field. UUID primary key.",
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AddIndex(
            model_name="label",
            index=models.Index(
                fields=["modified", "created"], name="edc_pylabel_modifie_01500a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="label",
            index=models.Index(
                fields=["user_modified", "user_created"], name="edc_pylabel_user_mo_cf698a_idx"
            ),
        ),
    ]
