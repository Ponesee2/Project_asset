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

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['first_name', 'last_name', 'designation', 'username', 'email', 'business_unit', 'department']
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#         # Populate the business unit and department dropdowns with all options
#             self.fields['business_unit'].queryset = BusinessUnit.objects.all()
#             self.fields['department'].queryset = Department.objects.all()

#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter first name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter last name' }),
#             'designation': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter designation'}),
#             'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter username'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter email'}),
#             'business_unit': forms.Select(attrs={'class': 'form-control','placeholder': 'Select business unit'}),
#             'department': forms.Select(attrs={'class': 'form-control','placeholder': 'Select department'}),
#         }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'designation', 'username', 'email', 'business_unit', 'department']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter designation'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'business_unit': forms.Select(attrs={'class': 'form-control', 'id': 'business_unit'}),
            'department': forms.Select(attrs={'class': 'form-control', 'id': 'department'}),
        }

    def __init__(self, *args, **kwargs):
        business_unit_id = kwargs.pop('business_unit_id', None)
        super().__init__(*args, **kwargs)
        
        # Populate business unit dropdown
        self.fields['business_unit'].queryset = BusinessUnit.objects.all()
        
        # Populate department dropdown based on business unit
        if self.instance.pk and self.instance.business_unit:
            self.fields['department'].queryset = Department.objects.filter(business_unit=self.instance.business_unit)
        elif business_unit_id:
            self.fields['department'].queryset = Department.objects.filter(business_unit_id=business_unit_id)
        else:
            self.fields['department'].queryset = Department.objects.none()

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
        fields = ['asset_category', 'asset_model', 'asset_tag', 'status',
                  'name', 'description', 'serial_number', 'image', 
                  'purchased_date', 'purchased_cost', 'supplier', 
                  'warranty_end_date', 'date', 'total_quantity', 'available_quantity']
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
            'status': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Status'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input Asset Name'
            }),
            'total_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input Total Quantity'
            }),
            'available_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input Available Quantity'
            }),
            'description': forms.TextInput(attrs={
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

# AssignedAssetFormSet = inlineformset_factory(
#     AssignedAssetTransaction, AssignedAsset,
#     fields=['asset', 'quantity'],
#     extra=1,  # One empty form to start with
#     widgets={
#         'asset': forms.Select(attrs={'class': 'form-control'}),
#         'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
#     }
# )
class AssignedAssetForm(forms.ModelForm):
    class Meta:
        model = AssignedAsset
        fields = ['asset', 'quantity_assigned']
        widgets = {
            'asset': forms.Select(attrs={'class': 'form-control'}),
            'quantity_assigned': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter to show only assets that are available and not archived
        self.fields['asset'].queryset = Asset.objects.filter(available_quantity__gt=0, is_archived=False)

    def clean_quantity_assigned(self):
        quantity_assigned = self.cleaned_data.get('quantity_assigned')
        asset = self.cleaned_data.get('asset')
        if asset and quantity_assigned > asset.available_quantity:
            raise forms.ValidationError(f"Cannot assign {quantity_assigned} units. Only {asset.available_quantity} units available.")
        return quantity_assigned

AssignedAssetFormSet = inlineformset_factory(
    AssignedAssetTransaction, AssignedAsset,
    form=AssignedAssetForm,
    extra=1
)