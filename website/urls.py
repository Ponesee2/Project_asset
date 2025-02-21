from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('unit', views.business_unit_list, name='business_unit_list'),
    path('create/', views.create_business_unit, name='create_business_unit'),
    path('update/<int:pk>/', views.update_business_unit, name='update_business_unit'),
    path('delete/<int:pk>/', views.delete_business_unit, name='delete_business_unit'),
    path('department', views.department_list, name='department_list'),
    path('create_department/', views.create_department, name='create_department'),
    path('update_department/<int:pk>/', views.update_department, name='update_department'),
    path('delete_department/<int:pk>/', views.delete_department, name='delete_department'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('employee', views.employee_list, name='employee_list'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('update_employee/<int:pk>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('asset-categories/', views.asset_category_list, name='asset_category_list'),
    path('asset-categories/create/', views.asset_category_create, name='asset_category_create'),
    path('asset-categories/<int:pk>/update/', views.asset_category_update, name='asset_category_update'),
    path('asset-categories/<int:pk>/delete/', views.asset_category_delete, name='asset_category_delete'),
    path('asset-models/', views.asset_model_list, name='asset_model_list'),
    path('asset-models/create/', views.asset_model_create, name='asset_model_create'),
    path('asset-models/<int:pk>/update/', views.asset_model_update, name='asset_model_update'),
    path('asset-models/<int:pk>/delete/', views.asset_model_delete, name='asset_model_delete'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/update/', views.supplier_update, name='supplier_update'),
    path('suppliers/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/create/', views.asset_create, name='asset_create'),
    path('assets/<int:pk>/edit/', views.asset_edit, name='asset_edit'),
    path('assets/<int:pk>/delete/', views.asset_delete, name='asset_delete'),
    path('filter-models/', views.filter_models, name='filter_models'),
    path("assignedasset", views.assigned_asset_list, name="assigned_asset_list"),
    path("assignedasset/", views.assigned_asset_create, name="assigned_asset_create"),
    path('assigned_asset/update/<int:pk>/', views.assigned_asset_update, name='assigned_asset_update'),
    path('assigned_asset/delete/<int:pk>/', views.assigned_asset_delete, name='assigned_asset_delete'),
    path('assigned_asset/detail/<int:pk>/', views.assigned_asset_detail, name='assigned_asset_detail'),
    path('get-departments/', views.get_departments, name='get_departments'),
    path('get_more_departments', views.get_more_departments, name='get_more_departments'),
    path('get-employees/', views.get_employees, name='get_employees'),
    path('assigned_asset/return/<int:assigned_asset_id>/', views.return_assigned_asset, name='return_assigned_asset'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    