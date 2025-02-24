
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


from django.db import transaction as db_transaction
from django.contrib import messages

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



# def return_assigned_asset(request, assigned_asset_id):
#     assigned_asset = get_object_or_404(AssignedAsset, id=assigned_asset_id)
    
#     # Update asset status
#     assigned_asset.asset.status = 'Available'
#     assigned_asset.asset.is_archived = False
#     assigned_asset.asset.save()
    
#     # Mark assigned asset as returned
#     assigned_asset.is_returned = True
#     assigned_asset.save()
    
#     messages.success(request, f"{assigned_asset.asset.name} has been returned successfully.")
    
#     # Pass it as a list to avoid iteration issues in the template
#     return render(request, "website/assigned_asset_returned.html", {'contexts': [assigned_asset]})

# from django.db import transaction
# def return_assigned_asset(request, transaction_id):
#     # Fetch all assigned assets for this transaction
#     assigned_assets = AssignedAsset.objects.filter(transaction_id=transaction_id, is_returned=False)

#     if not assigned_assets.exists():
#         messages.warning(request, "No assigned assets found for this transaction or they are already returned.")
#         return redirect('assigned_asset_list')

#     with transaction.atomic():
#         asset_names = []  # To store names of returned assets

#         for assigned_asset in assigned_assets:
#             if assigned_asset.asset:  # Ensure asset exists
#                 assigned_asset.asset.status = 'Available'
#                 assigned_asset.asset.is_archived = False
#                 assigned_asset.asset.save()

#             assigned_asset.is_returned = True
#             assigned_asset.save()

#             asset_names.append(assigned_asset.asset.name)

#     # Show success message listing all returned assets
#     messages.success(request, f"Assets returned successfully: {', '.join(asset_names)}")

#     return redirect('assigned_asset_list')\

from django.db import transaction
def return_assigned_assets(request, transaction_id):
    assigned_assets = AssignedAsset.objects.filter(transaction__transaction_id=transaction_id, is_returned=False)

    if not assigned_assets.exists():
        messages.warning(request, "No assigned assets found for this transaction or they are already returned.")
        return redirect('transaction_assets_list', transaction_id=transaction_id)

    with transaction.atomic():
        asset_names = []  

        for assigned_asset in assigned_assets:
            asset = assigned_asset.asset  # Assign to a variable for clarity
            if asset:
                asset.status = 'Available'
                asset.is_archived = False
                asset.save(update_fields=['status', 'is_archived'])  # 🔥 Ensures fields are updated

            assigned_asset.is_returned = True
            assigned_asset.save(update_fields=['is_returned'])  # 🔥 Save assigned asset properly

            if asset:
                asset_names.append(asset.name)

    messages.success(request, f"Assets returned successfully: {', '.join(asset_names)}")
    return redirect('transaction_assets_list', transaction_id=transaction_id)

def transaction_assets_list(request, transaction_id):
    transaction = AssignedAssetTransaction.objects.get(transaction_id=transaction_id)
    assigned_assets = AssignedAsset.objects.filter(transaction=transaction)

    return render(request, 'website/transaction_asset.html', {
        'transaction': transaction,
        'assigned_assets': assigned_assets
    })