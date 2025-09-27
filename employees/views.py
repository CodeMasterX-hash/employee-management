from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages

def employee_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        employees = Employee.objects.filter(name__icontains=search_query)
    else:
        employees = Employee.objects.all()
    return render(request, 'employees/index.html', {'employees': employees, 'search': search_query})

def employee_add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully!")
            return redirect('employee_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EmployeeForm()
    return render(request, 'employees/add.html', {'form': form})

def employee_edit(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully!")
            return redirect('employee_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EmployeeForm(instance=emp)
    return render(request, 'employees/edit.html', {'form': form})

def employee_delete(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    emp.delete()
    messages.success(request, "Employee deleted successfully!")
    return redirect('employee_list')
