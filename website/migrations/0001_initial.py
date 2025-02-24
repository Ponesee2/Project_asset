# Generated by Django 5.1.5 on 2025-02-13 03:16

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssignedAssetTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(editable=False, max_length=20, unique=True)),
                ('purpose', models.TextField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('manager', models.TextField(blank=True, max_length=100, null=True)),
                ('admin', models.TextField(blank=True, max_length=100, null=True)),
                ('corporatemanager', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('shortname', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
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
        migrations.CreateModel(
            name='AssetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('year_model', models.DateField(blank=True, null=True)),
                ('asset_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assetmodels', to='website.assetcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Assigned', 'Assigned'), ('Maintenance', 'Maintenance'), ('Disposed', 'Disposed'), ('Lost', 'Lost'), ('Stolen', 'Stolen')], default='Available', max_length=20)),
                ('asset_tag', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('purchased_date', models.DateField(blank=True, null=True)),
                ('purchased_cost', models.IntegerField(blank=True, null=True)),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('warranty_end_date', models.DateField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('asset_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='asset', to='website.assetcategory')),
                ('asset_model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='website.assetmodel')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='asset', to='website.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_assets', to='website.asset')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='website.assignedassettransaction')),
            ],
        ),
        migrations.AddField(
            model_name='assignedassettransaction',
            name='business_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_transactions', to='website.businessunit'),
        ),
        migrations.AddField(
            model_name='assignedassettransaction',
            name='business_unitfrom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transferred_from_transactions', to='website.businessunit'),
        ),
        migrations.AddField(
            model_name='assignedassettransaction',
            name='business_unitto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions_to', to='website.businessunit'),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='departments', to='website.businessunit')),
            ],
        ),
        migrations.AddField(
            model_name='assignedassettransaction',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_department_transactions', to='website.department'),
        ),
        migrations.AddField(
            model_name='assignedassettransaction',
            name='departmentfrom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transferred_from_department_transactions', to='website.department'),
        ),
        migrations.AddField(
            model_name='assignedassettransaction',
            name='departmentto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions_to', to='website.department'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('business_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='website.businessunit')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='website.department')),
            ],
        ),
        migrations.AddField(
            model_name='assignedassettransaction',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='website.employee'),
        ),
    ]
