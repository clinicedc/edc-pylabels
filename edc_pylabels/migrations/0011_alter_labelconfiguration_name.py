# Generated by Django 5.1.2 on 2024-11-13 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_pylabels", "0010_alter_labelconfiguration_requires_allocation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="labelconfiguration",
            name="name",
            field=models.CharField(
                help_text="Name of configuration registered with site_label_config.",
                max_length=50,
                unique=True,
                verbose_name="System config name",
            ),
        ),
    ]
