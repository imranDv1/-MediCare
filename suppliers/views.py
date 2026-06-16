from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from .models import Supplier
from .forms import SupplierForm


@login_required
def supplier_list(request):
    query = request.GET.get('q', '')
    suppliers = Supplier.objects.all()
    if query:
        suppliers = suppliers.filter(
            Q(name__icontains=query) | Q(contact_person__icontains=query)
        )
    for supplier in suppliers:
        supplier.medicine_count = supplier.medicines.count()
    context = {
        'suppliers': suppliers,
        'query': query,
    }
    return render(request, 'suppliers/supplier_list.html', context)


@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save()
            messages.success(request, f'Supplier "{supplier.name}" created successfully.')
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'suppliers/supplier_form.html', {'form': form})


@login_required
def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            supplier = form.save()
            messages.success(request, f'Supplier "{supplier.name}" updated successfully.')
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'suppliers/supplier_form.html', {'form': form, 'supplier': supplier})


@login_required
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    medicines = supplier.medicines.select_related('category').all()
    context = {
        'supplier': supplier,
        'medicines': medicines,
    }
    return render(request, 'suppliers/supplier_detail.html', context)


@login_required
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        name = supplier.name
        supplier.delete()
        messages.success(request, f'Supplier "{name}" deleted successfully.')
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': f'Supplier "{name}" deleted.'})
        return redirect('supplier_list')
    return redirect('supplier_list')
