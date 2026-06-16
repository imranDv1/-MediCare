from django.contrib import admin

from .models import Category, Medicine, StockMovement


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_filter = ['name']
    list_display = ['name', 'icon', 'medicine_count']

    def medicine_count(self, obj):
        return obj.medicines.count()
    medicine_count.short_description = 'Medicines'


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    search_fields = ['name', 'generic_name', 'brand', 'barcode_sku']
    list_filter = ['category', 'dosage_form', 'expiry_date', 'created_at']
    list_display = ['name', 'strength', 'category', 'price', 'stock_quantity', 'expiry_date', 'status']
    date_hierarchy = 'expiry_date'
    readonly_fields = ['barcode_sku', 'created_at', 'updated_at']

    def status(self, obj):
        return obj.status
    status.short_description = 'Status'


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    search_fields = ['medicine__name', 'note', 'user__username']
    list_filter = ['movement_type', 'timestamp']
    list_display = ['medicine', 'movement_type', 'quantity', 'user', 'timestamp']
    date_hierarchy = 'timestamp'
