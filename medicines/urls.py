from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicines/create/', views.medicine_create, name='medicine_create'),
    path('medicines/<int:pk>/', views.medicine_detail, name='medicine_detail'),
    path('medicines/<int:pk>/edit/', views.medicine_edit, name='medicine_edit'),
    path('medicines/<int:pk>/delete/', views.medicine_delete, name='medicine_delete'),
    path('stock/', views.stock_list, name='stock_list'),
    path('stock/restock/', views.restock_medicine, name='restock_medicine'),
    path('medicines/bulk-delete/', views.medicine_bulk_delete, name='medicine_bulk_delete'),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
]
