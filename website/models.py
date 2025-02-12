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
    image= models.ImageField(blank=True, null=True)
    purchased_date = models.DateField(blank=True, null=True)
    purchased_cost = models.IntegerField(blank=True, null=True)
    total_quantity = models.PositiveIntegerField(default=0)
    available_quantity = models.PositiveIntegerField(default=0)

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
    
# class AssignedAsset(models.Model):
#     asset = models.ForeignKey(
#         Asset, 
#         related_name='assigned_assets',  # More intuitive related name
#         on_delete=models.PROTECT, 
#         null=True, 
#         blank=True
#     )
#     quantity = models.IntegerField(blank=True, null=True)
#     business_unit = models.ForeignKey(
#         BusinessUnit, 
#         related_name='assigned_from',  # More intuitive related name
#         on_delete=models.PROTECT, 
#         null=True, 
#         blank=True
#     )

#     department = models.ForeignKey(
#         Department, 
#         related_name='assigned_from',
#         on_delete=models.PROTECT, 
#         null=True, 
#         blank=True
#     )

#     business_unitto = models.ForeignKey(
#         BusinessUnit, 
#         related_name='assigned_to',  # More intuitive related name
#         on_delete=models.PROTECT, 
#         null=True, 
#         blank=True
#     )

#     departmentto = models.ForeignKey(
#         Department, 
#         related_name='assigned_to',
#         on_delete=models.PROTECT, 
#         null=True, 
#         blank=True
#     )

#     employee = models.ForeignKey(
#         Employee, 
#         related_name='employee_assigned_assets',
#         on_delete=models.PROTECT, 
#         null=True, 
#         blank=True
#     )
     
#     purpose = models.TextField(max_length=100, blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     manager = models.TextField(max_length=100, blank=True, null=True)
#     admin = models.TextField(max_length=100, blank=True, null=True)
#     corporatemanager = models.TextField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return f"Asset: {self.asset}, Assigned to {self.employee}"

# class AssignedAssetTransaction(models.Model):
#     transaction_id = models.CharField(max_length=20, unique=True, editable=False)
#     business_unit = models.ForeignKey(BusinessUnit, related_name='transactions_from', on_delete=models.PROTECT)
#     department = models.ForeignKey(Department, related_name='transactions_from', on_delete=models.PROTECT)
#     employee = models.ForeignKey(Employee, related_name='transactions', on_delete=models.PROTECT)
#     business_unitfrom = models.ForeignKey(BusinessUnit, related_name='transactions_from', on_delete=models.PROTECT)
#     departmentform = models.ForeignKey(Department, related_name='transactions_from', on_delete=models.PROTECT)
#     business_unitto = models.ForeignKey(BusinessUnit, related_name='transactions_to', on_delete=models.PROTECT)
#     departmentto = models.ForeignKey(Department, related_name='transactions_to', on_delete=models.PROTECT)
#     purpose = models.TextField(max_length=100, blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     manager = models.TextField(max_length=100, blank=True, null=True)
#     admin = models.TextField(max_length=100, blank=True, null=True)
#     corporatemanager = models.TextField(max_length=100, blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if not self.transaction_id:
#             self.transaction_id = f"T{int(time.time())}"  # Unique Transaction ID
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"Transaction {self.transaction_id} for {self.employee}"

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
        related_name='transferred_from_department_transactions',  # Changed related_name
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

# class AssignedAsset(models.Model):
#     transaction = models.ForeignKey(AssignedAssetTransaction, related_name="assets", on_delete=models.CASCADE)
#     asset = models.ForeignKey(Asset, related_name='assigned_assets', on_delete=models.PROTECT)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} x {self.asset} (Transaction {self.transaction.transaction_id})"

# class AssignedAsset(models.Model):
#     transaction = models.ForeignKey(
#         AssignedAssetTransaction, 
#         related_name="assets", 
#         on_delete=models.CASCADE
#     )
#     asset = models.ForeignKey(
#         Asset, 
#         related_name='assigned_assets', 
#         on_delete=models.PROTECT
#     )
#     quantity_assigned = models.PositiveIntegerField(default=1)

#     def save(self, *args, **kwargs):
#         """Automatically update asset status and archive it when assigned."""
#         # Check if quantity assigned exceeds available stock
#         if self.quantity_assigned > self.asset.available_quantity:
#             raise ValueError(f"Cannot assign {self.quantity_assigned} units. Only {self.asset.available_quantity} available.")

#         # Deduct assigned quantity from available stock
#         self.asset.available_quantity -= self.quantity_assigned

#         # Archive asset only if all units are assigned
#         if self.asset.available_quantity == 0:
#             self.asset.is_archived = True
#             self.asset.status = Asset.StatusChoices.ASSIGNED
#         else:
#             self.asset.is_archived = False  # Unarchive if some stock remains
#             self.asset.status = Asset.StatusChoices.AVAILABLE  # Assume AVAILABLE is a status choice

#         self.asset.save()  # Save updated asset info

#         # Save the AssignedAsset instance
#         super().save(*args, **kwargs)

#     def delete(self, *args, **kwargs):
#         """Automatically restore asset availability when unassigned."""
#         # Add back the quantity to available stock
#         self.asset.available_quantity += self.quantity_assigned

#         # Unarchive asset if quantity is available again
#         if self.asset.available_quantity > 0:
#             self.asset.is_archived = False
#             self.asset.status = Asset.StatusChoices.AVAILABLE  # Restore status to AVAILABLE

#         self.asset.save()  # Save changes

#         # Delete the AssignedAsset instance
#         super().delete(*args, **kwargs)

#     def __str__(self):
#         return f"{self.quantity_assigned} x {self.asset} (Transaction {self.transaction.transaction_id})"

from django.db import transaction

class AssignedAsset(models.Model):
    transaction = models.ForeignKey(
        AssignedAssetTransaction, 
        related_name="assets", 
        on_delete=models.CASCADE
    )
    asset = models.ForeignKey(
        Asset, 
        related_name='assigned_assets', 
        on_delete=models.PROTECT
    )
    quantity_assigned = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        """Only save the AssignedAsset, do not modify available_quantity here."""
        super().save(*args, **kwargs)  # Save AssignedAsset instance

    def __str__(self):
        return f"{self.quantity_assigned} x {self.asset} (Transaction {self.transaction.transaction_id})"