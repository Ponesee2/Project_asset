# Generated by Django 5.1.5 on 2025-02-10 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_asset_status_delete_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
