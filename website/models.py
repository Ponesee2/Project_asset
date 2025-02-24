from django.db import models
from django.utils.timezone import now
import time
import random



class BusinessUnit(models.Model):
    name = models.CharField(max_length=100)
    shortname = models.CharField(blank=True , max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name) 

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    business_unit = models.ForeignKey(
        BusinessUnit, 
        on_delete=models.PROTECT,     
        related_name='departments'     
    )

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    business_unit = models.ForeignKey(
        BusinessUnit, 
        related_name='employees',  # More intuitive related name
        on_delete=models.PROTECT, 
        null=True, 
        blank=True
    )
    department = models.ForeignKey(
        Department, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class AssetCategory (models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    sub_category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class AssetModel(models.Model):
    asset_category = models.ForeignKey(
        AssetCategory, 
        related_name='assetmodels',  # More intuitive related name
        on_delete=models.PROTECT, 
        null=True, 
        blank=True
    )

    brand = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year_model = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.brand

class Supplier (models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    contact_person = models.CharField (max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Asset(models.Model):
    class StatusChoices(models.TextChoices):
        AVAILABLE = 'Available', 'Available'
        ASSIGNED = 'Assigned', 'Assigned'
        MAINTENANCE = 'Maintenance', 'Maintenance'
        DISPOSED = 'Disposed', 'Disposed'
        LOST = 'Lost', 'Lost'
        STOLEN = 'Stolen', 'Stolen'

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.AVAILABLE
    )
    
    asset_category = models.ForeignKey(
        AssetCategory, 
        related_name='asset',  # More intuitive related name
        on_delete=models.PROTECT, 
        null=True, 
        blank=True
    )

    asset_model = models.ForeignKey(
        AssetModel, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True
    )
    asset_tag = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)  
    purchased_date = models.DateField(blank=True, null=True)
    purchased_cost = models.IntegerField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)

    supplier = models.ForeignKey(
        Supplier, 
        related_name='asset',  # More intuitive related name
        on_delete=models.PROTECT, 
        null=True, 
        blank=True
    )

    warranty_end_date = models.DateField(blank=True, null=True)
    date = models.DateTimeField(default=now, blank=True, null=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class AssignedAssetTransaction(models.Model):
    transaction_id = models.CharField(max_length=20, unique=True, editable=False)
    
    business_unit = models.ForeignKey(
        BusinessUnit, 
        related_name='assigned_transactions',  # Changed related_name
        on_delete=models.PROTECT
    )
    
    department = models.ForeignKey(
        Department, 
        related_name='assigned_department_transactions',  # Changed related_name
        on_delete=models.PROTECT
    )
    
    employee = models.ForeignKey(
        Employee, 
        related_name='transactions', 
        on_delete=models.PROTECT
    )
    
    business_unitfrom = models.ForeignKey(
        BusinessUnit, 
        related_name='transferred_from_transactions',  # Changed related_name
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    
    departmentfrom = models.ForeignKey(
        Department, 
        related_name='transferred_from_department_transactions',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    
    business_unitto = models.ForeignKey(
        BusinessUnit, 
        related_name='transactions_to', 
        on_delete=models.PROTECT
    )
    
    departmentto = models.ForeignKey(
        Department, 
        related_name='transactions_to', 
        on_delete=models.PROTECT
    )
    
    purpose = models.TextField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    manager = models.TextField(max_length=100, blank=True, null=True)
    admin = models.TextField(max_length=100, blank=True, null=True)
    corporatemanager = models.TextField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = f"T{int(time.time())}"  # Unique Transaction ID
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.transaction_id} for {self.employee}"

class AssignedAsset(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('assigned', 'Assigned'),
    ]
    
    transaction = models.ForeignKey(
        AssignedAssetTransaction, 
        related_name="assets", 
        on_delete=models.CASCADE
    )
    asset = models.ForeignKey(
        Asset, 
        related_name='assigned_assets', 
        on_delete=models.CASCADE
    )
    is_returned = models.BooleanField(default=False) 

    def save(self, *args, **kwargs):
        # Only update the asset as assigned if it hasn't been marked as returned.
        if not self.is_returned:
            self.asset.status = Asset.StatusChoices.ASSIGNED  # Mark as Assigned
            self.asset.is_archived = True  # Archive the asset
            self.asset.save(update_fields=['status', 'is_archived'])
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.asset.name} - {self.transaction.transaction_id} (Assigned)"
 
    # def save(self, *args, **kwargs):
    #     # Assign the asset and archive it
    #     self.asset.status = Asset.StatusChoices.ASSIGNED  # Change status to Assigned
    #     self.asset.is_archived = True  # Archive the asset
    #     self.asset.save(update_fields=['status', 'is_archived'])# Save the asset update

    #     super().save(*args, **kwargs)  # Save AssignedAsset instance

    # def __str__(self):
    #     return f"{self.asset.name} - {self.transaction.transaction_id} (Assigned)"
    
from django.db.models.signals import pre_save
from django.dispatch import receiver
@receiver(pre_save, sender=Asset)
def enforce_asset_status(sender, instance, **kwargs):
    if instance.is_archived and instance.status not in [
        Asset.StatusChoices.AVAILABLE,
        Asset.StatusChoices.ASSIGNED,
    ]:
        instance.status = Asset.StatusChoices.DISPOSED