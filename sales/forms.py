from django import forms

from .models import Sale, SaleItem


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['patient_name', 'doctor_ref', 'payment_method', 'discount']
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Patient name (optional)'}),
            'doctor_ref': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor or prescription ref'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
        }

    def clean_discount(self):
        discount = self.cleaned_data.get('discount')
        if discount is not None and discount < 0:
            raise forms.ValidationError('Discount cannot be negative.')
        return discount


class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ['medicine', 'quantity', 'unit_price']
        widgets = {
            'medicine': forms.Select(attrs={'class': 'form-select medicine-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
        }


SaleItemFormSet = forms.inlineformset_factory(
    Sale,
    SaleItem,
    form=SaleItemForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True,
)
