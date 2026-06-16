from django.urls import path

from . import views

urlpatterns = [
    path('', views.sales_list, name='sales_list'),
    path('create/', views.create_sale, name='create_sale'),
    path('<int:pk>/', views.sale_detail, name='sale_detail'),
    path('<int:pk>/receipt/', views.print_receipt, name='print_receipt'),
    path('api/medicine-info/', views.get_medicine_info, name='get_medicine_info'),
]
