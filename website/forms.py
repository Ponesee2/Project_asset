from django import forms
from .models import *
from django.forms import inlineformset_factory

class BusinessUnitForm(forms.ModelForm):
    class Meta:
        model = BusinessUnit
        fields = ['name', 'shortname', 'location']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control' ,
                'size':  '50', 
                'placeholder': 'Enter business unit name'
            }),
            'shortname': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter short name'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter location'
            }),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'location', 'business_unit']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'size': '50',
                'placeholder': 'Enter department name'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter location'
            }),
            'business_unit': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select business unit'
            }),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'designation', 'username', 'email', 'business_unit', 'department']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        # Populate the business unit and department dropdowns with all options
            self.fields['business_unit'].queryset = BusinessUnit.objects.all()
            self.fields['department'].queryset = Department.objects.all()

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter designation'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
            'business_unit': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select business unit'
            }),
            'department': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select department'
            }),
        }

class AssetCategoryForm (forms.ModelForm):
    class Meta:
        model = AssetCategory
        fields = ['name', 'sub_category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Asset Category Name'
            }),
            'sub_category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Asset Category Sub Category Name'
            }),
        }

class AssetModelForm (forms.ModelForm):
    class Meta:
        model = AssetModel
        fields = ['asset_category', 'brand', 'model', 'year_model']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        # Populate the business unit and department dropdowns with all options
            self.fields['asset_category'].queryset = AssetCategory.objects.all()
        widgets = {
            'asset_category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Asset Category'
            }),
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Asset Brand Name'
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Asset Model Name'
            }),
           'year_model': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Year Model',
                    'type': 'date',  # Ensures the HTML5 date picker is used
            }),
        }

class SupplierForm (forms.ModelForm):
    class Meta: 
        model = Supplier
        fields = ['name', 'address', 'contact_person', 'contact_number']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Supplier Name'
            }), 
            'address' : forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the Address'
            }),
            'contact_person': forms.TextInput (attrs={
                'class': 'form-control',
                'placeholder': 'Enter Contact Person Name'
            }),
            'contact_number': forms.TextInput (attrs={
                'class': 'form-control',
                'placeholder': 'Enter Contact Number'
            })
        }

class AssetForm (forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_category', 'asset_model', 'asset_tag', 
                  'name', 'description', 'serial_number', 'image', 
                  'purchased_date', 'purchased_cost','quantity', 'supplier', 
                  'warranty_end_date', 'date']
        widgets = {
            'asset_category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Asset Category'
            }),
            'asset_model': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Asset Model'
            }),
            'asset_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input Asset Tag'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input Asset Name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input Description'
            }),
            'serial_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input Serial Number'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input Image'
            }),
            'purchased_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input Purchased Date',
                'type': 'date', 
            }),
            'purchased_cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Purchased Cost'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Quantity'
            }),
            'supplier': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Supplier'
            }),
            'warranty_end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input Warranty End Date',
                'type': 'date', 
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Set Date',
                'type': 'date', 
            })
        }

# class AssignedAssetForm (forms.ModelForm):
#     class Meta:
#         model = AssignedAsset
#         fields = ['asset', 'business_unit', 'department', 'employee', 'business_unitto', 'departmentto', 'purpose', 'date', 'manager', 'admin', 'corporatemanager']
#         widgets = {
#             'asset': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Select Asset',
#             }),
#             'business_unit': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Select Business Unit of Asset'
#             }),
#             'department': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Select Department of Asset'
#             }),
#             'employee': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Select Employee'
#             }),
#             'business_unitto': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Select Business Unit to Transfer'
#             }),
#             'departmentto': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Select Business Unit to Transfer'
#             }),
#             'purpose': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'What the Purpose or Use',
#             }),
#             'date': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Date Select',
#                 'type':  'date'
#             }),
#               'manager': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Input Dept./ Gen Manager',
#             }),
#               'admin': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'IT Asset Administrator',
#             }),
#              'corporatemanager': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Corporate IT Manager',
#             }),
#         }

# class AssignedAssetForm(forms.ModelForm):
#     asset = forms.ModelMultipleChoiceField(
#         queryset=Asset.objects.all(),
#         widget=forms.CheckboxSelectMultiple,  # Allows multiple selection
#     )

#     class Meta:
#         model = AssignedAsset
#         fields = ['asset', 'business_unit', 'department', 'employee', 
#                   'business_unitto', 'departmentto', 'purpose', 'date', 
#                   'manager', 'admin', 'corporatemanager']
#         widgets = {
#             'business_unit': forms.Select(attrs={'class': 'form-control'}),
#             'department': forms.Select(attrs={'class': 'form-control'}),
#             'employee': forms.Select(attrs={'class': 'form-control'}),
#             'business_unitto': forms.Select(attrs={'class': 'form-control'}),
#             'departmentto': forms.Select(attrs={'class': 'form-control'}),
#             'purpose': forms.TextInput(attrs={'class': 'form-control'}),
#             'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'manager': forms.TextInput(attrs={'class': 'form-control'}),
#             'admin': forms.TextInput(attrs={'class': 'form-control'}),
#             'corporatemanager': forms.TextInput(attrs={'class': 'form-control'}),
#         }

class AssignedAssetTransactionForm(forms.ModelForm):
    class Meta:
        model = AssignedAssetTransaction
        fields = ['business_unit', 'department', 'employee', 
                  'business_unitto', 'departmentto', 'purpose', 'date',
                  'manager', 'admin', 'corporatemanager']
        widgets = {
            'business_unit': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'business_unitto': forms.Select(attrs={'class': 'form-control'}),
            'departmentto': forms.Select(attrs={'class': 'form-control'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'manager': forms.TextInput(attrs={'class': 'form-control'}),
            'admin': forms.TextInput(attrs={'class': 'form-control'}),
            'corporatemanager': forms.TextInput(attrs={'class': 'form-control'}),
        }

AssignedAssetFormSet = inlineformset_factory(
    AssignedAssetTransaction, AssignedAsset,
    fields=['asset', 'quantity'],
    extra=1,  # One empty form to start with
    widgets={
        'asset': forms.Select(attrs={'class': 'form-control'}),
        'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
    }
)