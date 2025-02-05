
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import *
from .forms import *


def dashboard(request):
    return render(request, 'website/index.html', {})


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
    business_units = BusinessUnit.objects.all()
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

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
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

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'website/employee_detail.html', {'employee': employee})

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


def assigned_asset_create(request):
    if request.method == "POST":
        transaction_form = AssignedAssetTransactionForm(request.POST)
        asset_formset = AssignedAssetFormSet(request.POST)

        if transaction_form.is_valid() and asset_formset.is_valid():
            transaction = transaction_form.save()  # Save transaction first
            asset_instances = asset_formset.save(commit=False)
            for asset in asset_instances:
                asset.transaction = transaction  # Link assets to transaction
                asset.save()
            return redirect("assigned_asset_list")

    else:
        transaction_form = AssignedAssetTransactionForm()
        asset_formset = AssignedAssetFormSet()

    return render(request, "website/assigned_asset_form.html", {
        "transaction_form": transaction_form,
        "asset_formset": asset_formset
    })

def assigned_asset_update(request, pk):
    transaction = get_object_or_404(AssignedAssetTransaction, pk=pk)
    if request.method == "POST":
        transaction_form = AssignedAssetTransactionForm(request.POST, instance=transaction)
        asset_formset = AssignedAssetFormSet(request.POST, instance=transaction)

        if transaction_form.is_valid() and asset_formset.is_valid():
            transaction = transaction_form.save()
            asset_instances = asset_formset.save(commit=False)
            for asset in asset_instances:
                asset.transaction = transaction
                asset.save()
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