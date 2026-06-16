from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports_dashboard, name='reports_dashboard'),
    path('sales/', views.sales_report, name='sales_report'),
    path('inventory/', views.inventory_report, name='inventory_report'),
    path('expiry/', views.expiry_report, name='expiry_report'),
    path('categories/', views.category_report, name='category_report'),
    path('export/sales/csv/', views.export_sales_csv, name='export_sales_csv'),
    path('export/inventory/csv/', views.export_inventory_csv, name='export_inventory_csv'),
    path('export/sales/pdf/', views.export_sales_pdf, name='export_sales_pdf'),
    path('export/inventory/pdf/', views.export_inventory_pdf, name='export_inventory_pdf'),
]
