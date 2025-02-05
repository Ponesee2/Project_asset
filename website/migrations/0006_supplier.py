# Generated by Django 5.1.5 on 2025-01-28 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_assetmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
