
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction as db_transaction
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.db.models import Sum
from .models import *
from .forms import *


def dashboard(request):
    business_unit_count = BusinessUnit.objects.count()
    department_count = Department.objects.count()
    employee_count = Employee.objects.count()
    asset_category_count = AssetCategory.objects.count()
    asset_model_count = AssetModel.objects.count()
    asset_count = Asset.objects.count()
    supplier_count = Supplier.objects.count()
    assigned_asset_count = AssignedAsset.objects.count()
    business_units = BusinessUnit.objects.annotate() 
    context = {
        'business_unit_count': business_unit_count,
        'department_count': department_count,
        'employee_count': employee_count,
        'asset_category_count': asset_category_count,
        'asset_model_count': asset_model_count,
        'asset_count': asset_count,
        'supplier_count': supplier_count,
        'business_units': business_units,
        'assigned_asset_count': assigned_asset_count
    }   
    return render(request, 'website/index.html', context)
# Create a new BusinessUnit
def create_business_unit(request):
    if request.method == 'POST':
        form = BusinessUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business_unit_list')
    else:
        form = BusinessUnitForm()
    return render(request, 'website/business_unit_form.html', {'form': form})

# List all BusinessUnits
def business_unit_list(request):
    business_units = BusinessUnit.objects.annotate()    
    return render(request, 'website/business_unit_list.html', {'business_units': business_units})

# Update a BusinessUnit
def update_business_unit(request, pk):
    business_unit = get_object_or_404(BusinessUnit, pk=pk)
    if request.method == 'POST':
        form = BusinessUnitForm(request.POST, instance=business_unit)
        if form.is_valid():
            form.save()
            return redirect('business_unit_list')
    else:
        form = BusinessUnitForm(instance=business_unit)
    return render(request, 'website/business_unit_form.html', {'form': form})

# Delete a BusinessUnit
def delete_business_unit(request, pk):
    business_unit = get_object_or_404(BusinessUnit, pk=pk)
    if request.method == 'POST':
        business_unit.delete()
        return redirect('business_unit_list')
    return render(request, 'website/business_unit_confirm_delete.html', {'business_unit': business_unit})

def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'website/department_form.html', {'form': form})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'website/department_list.html', {'departments': departments})

def update_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'website/department_form.html', {'form': form})

def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'website/department_confirm_delete.html', {'department': department})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'website/department_detail.html', {'department': department})

# def create_employee(request):

#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('employee_list')
#     else:
#         form = EmployeeForm()
#     return render(request, 'website/employee_form.html', {'form': form})

def create_employee(request):
    business_unit_id = request.POST.get('business_unit') if request.method == 'POST' else None
    if request.method == 'POST':
        form = EmployeeForm(request.POST, business_unit_id=business_unit_id)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(business_unit_id=business_unit_id)
    return render(request, 'website/employee_form.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'website/employee_list.html', {'employees': employees})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'website/employee_form.html', {'form': form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'website/employee_confirm_delete.html', {'employee': employee})

# def employee_detail(request, pk):
#     employee = get_object_or_404(Employee, pk=pk)
#     return render(request, 'website/employee_detail.html', {'employee': employee})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    assigned_assets = AssignedAsset.objects.filter(transaction__employee=employee)
    return render(request, 'website/employee_detail.html', {
        'employee': employee,
        'assigned_assets': assigned_assets
    })

def asset_category_create(request):
    if request.method == 'POST':
        form = AssetCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_category_list')  # Redirect to list view
    else:
        form = AssetCategoryForm()
    return render(request, 'website/asset_category_form.html', {'form': form})

# List all AssetCategories
def asset_category_list(request):
    categories = AssetCategory.objects.all()
    return render(request, 'website/asset_category_list.html', {'categories': categories})

# Update an existing AssetCategory
def asset_category_update(request, pk):
    category = get_object_or_404(AssetCategory, pk=pk)
    if request.method == 'POST':
        form = AssetCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('asset_category_list')
    else:
        form = AssetCategoryForm(instance=category)
    return render(request, 'website/asset_category_form.html', {'form': form})

# Delete an AssetCategory
def asset_category_delete(request, pk):
    category = get_object_or_404(AssetCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('asset_category_list')
    return render(request, 'website/asset_category_confirm_delete.html', {'category': category})

# Create a new AssetModel
def asset_model_create(request):
    if request.method == 'POST':
        form = AssetModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_model_list')  # Redirect to list view
    else:
        form = AssetModelForm()
    return render(request, 'website/asset_model_form.html', {'form': form})

# List all AssetModels
def asset_model_list(request):
    asset_models = AssetModel.objects.all()
    return render(request, 'website/asset_model_list.html', {'asset_models': asset_models})

# Update an existing AssetModel
def asset_model_update(request, pk):
    asset_model = get_object_or_404(AssetModel, pk=pk)
    if request.method == 'POST':
        form = AssetModelForm(request.POST, instance=asset_model)
        if form.is_valid():
            form.save()
            return redirect('asset_model_list')
    else:
        form = AssetModelForm(instance=asset_model)
    return render(request, 'website/asset_model_form.html', {'form': form})

# Delete an AssetModel
def asset_model_delete(request, pk):
    asset_model = get_object_or_404(AssetModel, pk=pk)
    if request.method == 'POST':
        asset_model.delete()
        return redirect('asset_model_list')
    return render(request, 'website/asset_model_confirm_delete.html', {'asset_model': asset_model})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')  # Redirect to list view after saving
    else:
        form = SupplierForm()
    return render(request, 'website/supplier_form.html', {'form': form})

# List all Suppliers
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'website/supplier_list.html', {'suppliers': suppliers})

# Update an existing Supplier
def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'website/supplier_form.html', {'form': form})

# Delete a Supplier
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'website/supplier_confirm_delete.html', {'supplier': supplier})

def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)  # Handle image uploads
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm()
    return render(request, 'website/asset_form.html', {'form': form, 'action': 'Create Asset'})

def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'website/asset_list.html', {'assets': assets})
   
def asset_edit(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES, instance=asset)
        if form.is_valid(): 
            form.save()
            return redirect ('asset_list')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'website/asset_form.html', {'form': form})

def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk) 
    if request.method == 'POST':
        asset.delete()
        return redirect ('asset_list')
    return render(request, 'website/asset_delete.html', {'asset': asset})

def filter_models(request):
    category_id = request.GET.get('category_id')  # Get the selected category ID
    brands = AssetModel.objects.filter(asset_category_id=category_id)  # Filter models by category
    brand_data = [{'id': brand.id, 'name': brand.brand} for brand in brands]
    return JsonResponse({'brands': brand_data})

def assigned_asset_list(request):
    transactions = AssignedAssetTransaction.objects.prefetch_related('assets')
    return render(request, "website/assigned_asset_list.html", {"transactions": transactions})


# def assigned_asset_create(request):
#     if request.method == "POST":
#         transaction_form = AssignedAssetTransactionForm(request.POST)
#         asset_formset = AssignedAssetFormSet(request.POST)

#         if transaction_form.is_valid() and asset_formset.is_valid():
#             transaction = transaction_form.save()  # Save transaction first
#             asset_instances = asset_formset.save(commit=False)
#             for asset in asset_instances:
#                 asset.transaction = transaction  # Link assets to transaction
#                 asset.save()
#             return redirect("assigned_asset_list")
#     else:
#         transaction_form = AssignedAssetTransactionForm()
#         asset_formset = AssignedAssetFormSet()

#     return render(request, "website/assigned_asset_form.html", {
#         "transaction_form": transaction_form,
#         "asset_formset": asset_formset
#     })

# def assigned_asset_update(request, pk):
#     transaction = get_object_or_404(AssignedAssetTransaction, pk=pk)
#     if request.method == "POST":
#         transaction_form = AssignedAssetTransactionForm(request.POST, instance=transaction)
#         asset_formset = AssignedAssetFormSet(request.POST, instance=transaction)

#         if transaction_form.is_valid() and asset_formset.is_valid():
#             transaction = transaction_form.save()
#             asset_instances = asset_formset.save(commit=False)
#             for asset in asset_instances:
#                 asset.transaction = transaction
#                 asset.save()
#             return redirect("assigned_asset_list")
#     else:
#         transaction_form = AssignedAssetTransactionForm(instance=transaction)
#         asset_formset = AssignedAssetFormSet(instance=transaction)
#     return render(request, "website/assigned_asset_form.html", {
#         "transaction_form": transaction_form,
#         "asset_formset": asset_formset,
#     })

# def assigned_asset_create(request):
#     business_unit_id = request.POST.get('business_unit') if request.method == 'POST' else None

#     if request.method == "POST":
#         transaction_form = AssignedAssetTransactionForm(request.POST, business_unit_id=business_unit_id)
#         asset_formset = AssignedAssetFormSet(request.POST)

#         if transaction_form.is_valid() and asset_formset.is_valid():
#             transaction = transaction_form.save()
#             asset_instances = asset_formset.save(commit=False)

#             for assigned_asset in asset_instances:
#                 asset = assigned_asset.asset
#                 if assigned_asset.quantity_assigned <= asset.available_quantity:
#                     assigned_asset.transaction = transaction
#                     asset.available_quantity -= assigned_asset.quantity_assigned
#                     if asset.available_quantity == 0:
#                         asset.is_archived = True  # Optionally archive the asset
#                     asset.save()
#                     assigned_asset.save()
#                 else:
#                     # Handle the case where assigned quantity exceeds available quantity
#                     # This should be caught by form validation, but included here for safety
#                     pass

#             return redirect("assigned_asset_list")
#     else:
#         transaction_form = AssignedAssetTransactionForm()
#         asset_formset = AssignedAssetFormSet()

#     return render(request, "website/assigned_asset_form.html", {
#         "transaction_form": transaction_form,
#         "asset_formset": asset_formset
#     })

from django.contrib import messages

# def assigned_asset_create(request):
#     business_unit_id = request.POST.get('business_unit') if request.method == 'POST' else request.GET.get('business_unit')

#     if request.method == "POST":
#         transaction_form = AssignedAssetTransactionForm(request.POST, business_unit_id=business_unit_id)
#         asset_formset = AssignedAssetFormSet(request.POST)

#         if transaction_form.is_valid() and asset_formset.is_valid():
#             transaction = transaction_form.save(commit=False)
#             transaction.save()  # Save transaction first before assigning assets
            
#             asset_instances = asset_formset.save(commit=False)
#             insufficient_assets = []  # Track assets with insufficient quantity

#             for assigned_asset in asset_instances:
#                 asset = assigned_asset.asset

#                 if assigned_asset.quantity_assigned > asset.available_quantity:
#                     insufficient_assets.append(asset.name)
#                 else:
#                     assigned_asset.transaction = transaction
#                     asset.available_quantity -= assigned_asset.quantity_assigned
#                     if asset.available_quantity == 0:
#                         asset.is_archived = True  # Optionally archive the asset

#             # If there are insufficient assets, display error and reload the form
#             if insufficient_assets:
#                 messages.error(request, f"Not enough quantity available for: {', '.join(insufficient_assets)}")
#                 return render(request, "website/assigned_asset_form.html", {
#                     "transaction_form": transaction_form,
#                     "asset_formset": asset_formset
#                 })

#             # If no errors, save all assigned assets and update inventory efficiently
#             for assigned_asset in asset_instances:
#                 assigned_asset.save()
#             Asset.objects.bulk_update([a.asset for a in asset_instances], ["available_quantity", "is_archived"])

#             messages.success(request, "Assets successfully assigned.")
#             return redirect("assigned_asset_list")

#     else:
#         transaction_form = AssignedAssetTransactionForm(business_unit_id=business_unit_id)
#         asset_formset = AssignedAssetFormSet()

#     return render(request, "website/assigned_asset_form.html", {
#         "transaction_form": transaction_form,
#         "asset_formset": asset_formset
#     })

# def assigned_asset_create(request):
#     business_unit_id = request.POST.get('business_unit') if request.method == 'POST' else request.GET.get('business_unit')

#     if request.method == "POST":
#         transaction_form = AssignedAssetTransactionForm(request.POST, business_unit_id=business_unit_id)
#         asset_formset = AssignedAssetFormSet(request.POST)

#         if transaction_form.is_valid() and asset_formset.is_valid():
#             transaction = transaction_form.save(commit=False)
#             transaction.save()  # Save transaction first

#             asset_instances = asset_formset.save(commit=False)
#             insufficient_assets = []

#             for assigned_asset in asset_instances:
#                 asset = assigned_asset.asset

#                 if assigned_asset.quantity_assigned > asset.available_quantity:
#                     insufficient_assets.append(asset.name)
#                 else:
#                     assigned_asset.transaction = transaction
#                     asset.available_quantity -= assigned_asset.quantity_assigned
#                     if asset.available_quantity == 0:
#                         asset.is_archived = True  # Optionally archive the asset

#             if insufficient_assets:
#                 messages.error(request, f"Not enough quantity available for: {', '.join(insufficient_assets)}")
#                 return render(request, "website/assigned_asset_form.html", {
#                     "transaction_form": transaction_form,
#                     "asset_formset": asset_formset
#                 })

#             # Save assigned assets and update asset inventory
#             for assigned_asset in asset_instances:
#                 assigned_asset.save()

#             assets_to_update = Asset.objects.filter(id__in=[a.asset.id for a in asset_instances])
#             for asset in assets_to_update:
#                 asset.save()

#             messages.success(request, "Assets successfully assigned.")
#             return redirect("assigned_asset_list")

#     else:
#         transaction_form = AssignedAssetTransactionForm(business_unit_id=business_unit_id)
#         asset_formset = AssignedAssetFormSet()

#     return render(request, "website/assigned_asset_form.html", {
#         "transaction_form": transaction_form,
#         "asset_formset": asset_formset
#     })

# def assigned_asset_create(request):
#     if request.method == "POST":
#         # Get the business_unit value from POST data
#         business_unit_id = request.POST.get('business_unit')
        
#         # Initialize the transaction form with the POST data and any additional parameters
#         transaction_form = AssignedAssetTransactionForm(request.POST, business_unit_id=business_unit_id)
        
#         # Validate the transaction form first so we can get the parent instance.
#         if transaction_form.is_valid():
#             # Get an unsaved instance of the transaction
#             transaction = transaction_form.save(commit=False)
#             # Initialize the asset inline formset with the POST data and the parent instance
#             asset_formset = AssignedAssetFormSet(request.POST, instance=transaction)
#         else:
#             # If the transaction form isn't valid, initialize the formset without an instance.
#             asset_formset = AssignedAssetFormSet(request.POST)
        
#         # Now check that both the transaction form and the asset formset are valid.
#         if transaction_form.is_valid() and asset_formset.is_valid():
#             # Save the parent instance
#             transaction.save()
            
#             # Save the asset formset but do not commit immediately
#             asset_instances = asset_formset.save(commit=False)
#             insufficient_assets = []
            
#             # Process each asset assignment
#             for assigned_asset in asset_instances:
#                 asset = assigned_asset.asset
#                 if assigned_asset.quantity_assigned > asset.available_quantity:
#                     insufficient_assets.append(asset.name)
#                 else:
#                     # Associate the asset with the transaction
#                     assigned_asset.transaction = transaction
#                     # Deduct the assigned quantity from the asset’s available quantity
#                     asset.available_quantity -= assigned_asset.quantity_assigned
#                     if asset.available_quantity == 0:
#                         asset.is_archived = True  # Optionally archive the asset
            
#             if insufficient_assets:
#                 # If there are any issues with asset quantities, display an error message
#                 from django.contrib import messages
#                 messages.error(request, f"Not enough quantity available for: {', '.join(insufficient_assets)}")
#                 return render(request, "website/assigned_asset_form.html", {
#                     "transaction_form": transaction_form,
#                     "asset_formset": asset_formset
#                 })
            
#             # Save each assigned asset
#             for assigned_asset in asset_instances:
#                 assigned_asset.save()
            
#             # Save updated asset details
#             for asset in {a.asset for a in asset_instances}:
#                 asset.save()
            
#             from django.contrib import messages
#             messages.success(request, "Assets successfully assigned.")
#             return redirect("assigned_asset_list")
        
#     else:
#         # On GET, try to pick up the business_unit from the GET parameters (if available)
#         business_unit_id = request.GET.get('business_unit')
#         transaction_form = AssignedAssetTransactionForm(business_unit_id=business_unit_id)
#         # Create a new (unsaved) parent instance for the formset to bind to
#         transaction_instance = AssignedAssetTransaction()
#         asset_formset = AssignedAssetFormSet(instance=transaction_instance)
    
#     return render(request, "website/assigned_asset_form.html", {
#         "transaction_form": transaction_form,
#         "asset_formset": asset_formset
#     })

# def assigned_asset_create(request):
#     if request.method == "POST":
#         transaction_form = AssignedAssetTransactionForm(request.POST)
#         asset_formset = AssignedAssetFormSet(request.POST)

#         if transaction_form.is_valid() and asset_formset.is_valid():
#             with db_transaction.atomic():  # Ensures atomic operations
#                 transaction = transaction_form.save()
#                 asset_instances = asset_formset.save(commit=False)

#                 assigned_assets = set()

#                 for assigned_asset in asset_instances:
#                     asset = assigned_asset.asset

#                     if asset.id in assigned_assets:
#                         messages.error(request, f"Duplicate assignment detected for asset: {asset.name}")
#                         return render(
#                             request, "website/assigned_asset_form.html",
#                             {"transaction_form": transaction_form, "asset_formset": asset_formset}
#                         )

#                     assigned_assets.add(asset.id)
#                     assigned_asset.transaction = transaction
#                     assigned_asset.save()

#                 messages.success(request, "Assets successfully assigned.")
#                 return redirect("assigned_asset_list")

#         messages.error(request, "Please correct the errors below.")

#     else:  # GET request
#         transaction_form = AssignedAssetTransactionForm()
#         transaction_instance = AssignedAssetTransaction()
#         asset_formset = AssignedAssetFormSet(instance=transaction_instance)

#     return render(
#         request, "website/assigned_asset_form.html",
#         {"transaction_form": transaction_form, "asset_formset": asset_formset}
#     )

from django.db import transaction as db_transaction



def assigned_asset_create(request):
    if request.method == "POST":
        transaction_form = AssignedAssetTransactionForm(request.POST)
        asset_formset = AssignedAssetFormSet(request.POST)
        print(request.POST)
        if transaction_form.is_valid() and asset_formset.is_valid():
            try:
                with db_transaction.atomic():  # Atomic transaction ensures all saves succeed
                    transaction = transaction_form.save()

                    asset_instances = asset_formset.save(commit=False)
                    for assigned_asset in asset_instances:
                        assigned_asset.transaction = transaction
                        assigned_asset.asset.status = Asset.StatusChoices.ASSIGNED  # Set status
                        assigned_asset.asset.is_archived = True  # Archive asset
                        assigned_asset.asset.save()  # Save asset update
                        assigned_asset.save()  # Save assigned asset record
                        print(request.POST)

                    messages.success(request, "Assets successfully assigned and archived.")
                    return redirect("assigned_asset_list")
                

            except Exception as e:
                print(f"Database error: {e}")  # Debugging
                messages.error(request, f"An error occurred while saving: {e}")
            else:
                    print(transaction_form.errors)  # Debugging
                    print(asset_formset.errors)  # Debugging
        else:
            print("Transaction Form Errors:", transaction_form.errors)  # Debugging
            print("Formset Errors:", asset_formset.errors)  # Debugging
            messages.error(request, "Please correct the errors below.")
        print(request.POST)

    else:
        transaction_form = AssignedAssetTransactionForm()
        asset_formset = AssignedAssetFormSet()

    return render(request, "website/assigned_asset_form.html", {
        "transaction_form": transaction_form,
        "asset_formset": asset_formset,
    })

def assigned_asset_update(request, pk):
    transaction = get_object_or_404(AssignedAssetTransaction, pk=pk)

    if request.method == "POST":
        transaction_form = AssignedAssetTransactionForm(request.POST, instance=transaction)
        asset_formset = AssignedAssetFormSet(request.POST, instance=transaction)

        if transaction_form.is_valid() and asset_formset.is_valid():
            transaction = transaction_form.save()
            asset_instances = asset_formset.save(commit=False)

            for assigned_asset in asset_instances:
                assigned_asset.transaction = transaction
                assigned_asset.asset.status = "Assigned"  # Update asset status
                assigned_asset.asset.is_archived = True  # Archive the asset
                assigned_asset.asset.save()  # Save the updated asset
                assigned_asset.save()  # Save assigned asset record

            return redirect("assigned_asset_list")
    else:
        transaction_form = AssignedAssetTransactionForm(instance=transaction)
        asset_formset = AssignedAssetFormSet(instance=transaction)

    return render(request, "website/assigned_asset_form.html", {
        "transaction_form": transaction_form,
        "asset_formset": asset_formset,
    })


def assigned_asset_delete(request, pk):
    transaction = get_object_or_404(AssignedAssetTransaction, pk=pk)
    if request.method == "POST":
        transaction.delete()
        return redirect("assigned_asset_list")
    return render(request, "website/assigned_asset_confirm_delete.html", {"transaction": transaction})

def assigned_asset_detail(request, pk):
    transaction = get_object_or_404(AssignedAssetTransaction, pk=pk)
    return render(request, "website/assigned_asset_detail.html", {"transaction": transaction})

def get_departments(request):
    business_unit_id = request.GET.get('business_unit_id')
    departments = Department.objects.filter(business_unit_id=business_unit_id).values('id', 'name')
    return JsonResponse(list(departments), safe=False)

def get_more_departments(request):
    business_unit_id = request.GET.get('business_unit_id')
    
    if business_unit_id:
        departments_qs = Department.objects.filter(business_unit_id=business_unit_id)
    else:
        departments_qs = Department.objects.none()
    
    departments = [
        {"id": dept.id, "name": dept.name}  # Adjust these fields as needed
        for dept in departments_qs
    ]
    
    return JsonResponse({"departments": departments})

from django.views.decorators.http import require_GET

@require_GET
def get_employees(request):
    department_id = request.GET.get('department_id')
    
    if department_id:
        employees_qs = Employee.objects.filter(department_id=department_id)
    else:
        employees_qs = Employee.objects.none()
    
    employees = [
        {
            "id": emp.id,
            "name": f"{emp.first_name} {emp.last_name}"  # Combine first and last name
        }
        for emp in employees_qs
    ]
    
    return JsonResponse({"employees": employees})  



def return_assigned_asset(request, assigned_asset_id):
    assigned_asset = get_object_or_404(AssignedAsset, id=assigned_asset_id)
    
    # Update asset status
    assigned_asset.asset.status = 'Available'
    assigned_asset.asset.is_archived = False
    assigned_asset.asset.save()
    
    # Mark assigned asset as returned
    assigned_asset.is_returned = True
    assigned_asset.save()
    
    messages.success(request, f"{assigned_asset.asset.name} has been returned successfully.")
    
    # Pass it as a list to avoid iteration issues in the template
    return render(request, "website/assigned_asset_returned.html", {'contexts': [assigned_asset]})