from django import forms

from .models import Category, Medicine, StockMovement


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        exclude = ['created_by']
        widgets = {
            'manufacturing_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return price

    def clean_stock_quantity(self):
        stock = self.cleaned_data.get('stock_quantity')
        if stock is not None and stock < 0:
            raise forms.ValidationError('Stock quantity cannot be negative.')
        return stock

    def clean(self):
        cleaned_data = super().clean()
        expiry = cleaned_data.get('expiry_date')
        manufacturing = cleaned_data.get('manufacturing_date')

        if expiry and manufacturing and expiry <= manufacturing:
            raise forms.ValidationError('Expiry date must be after manufacturing date.')

        return cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = ['medicine', 'movement_type', 'quantity', 'note']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 2}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity <= 0:
            raise forms.ValidationError('Quantity must be greater than zero.')
        return quantity
