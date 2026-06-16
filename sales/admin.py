from django.contrib import admin

from .models import Sale, SaleItem


class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 0
    readonly_fields = ['medicine', 'quantity', 'unit_price', 'subtotal']
    can_delete = False


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['invoice_no', 'patient_name', 'payment_method', 'subtotal', 'discount', 'total', 'user', 'timestamp']
    list_filter = ['payment_method', 'timestamp']
    search_fields = ['invoice_no', 'patient_name', 'doctor_ref']
    readonly_fields = ['invoice_no', 'subtotal', 'total', 'user', 'timestamp']
    inlines = [SaleItemInline]
    date_hierarchy = 'timestamp'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ['sale', 'medicine', 'quantity', 'unit_price', 'subtotal']
    search_fields = ['sale__invoice_no', 'medicine__name']
    list_filter = ['sale__timestamp']
