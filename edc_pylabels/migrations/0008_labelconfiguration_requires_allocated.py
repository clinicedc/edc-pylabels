# Generated by Django 5.1.2 on 2024-11-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_pylabels", "0007_alter_labelconfiguration_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="labelconfiguration",
            name="requires_allocated",
            field=models.BooleanField(default=False),
        ),
    ]