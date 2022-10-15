from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout

from userapp.models import Employee
from .forms import EmployeeForm

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username =email, password=password)
            if user is not None:
                login(request, user)
                return redirect('add_employee')
            else:
                return redirect('user_login')
    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request,'userapp/login.html',context)

def user_logout(request):
    logout(request)
    return redirect('user_login')

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            # return render(request,'userapp/add_salary.html',context)
            return redirect('add_salary')
        else:
            messages.info(request, "Invalid data")
            return render(request,'userapp/employee-form.html',context)
    form = EmployeeForm()
    context = {'form':form,}
    return render(request,'userapp/employee-form.html',context)

def add_salary(request):
    if request.method == 'POST':
        employee = Employee.objects.all().last()
        salary = request.POST['salary']
        employee.salary = salary
        employee.save()
        context = {'employee':employee}
        return redirect('employee_listing')
    try:
        employee = Employee.objects.all().last()
    except Employee.DoesNotExist:
        employee = None
    context = {'employee':employee}
    return render(request,'userapp/add_salary.html',context)

def employee_listing(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    return render(request,'userapp/employee_index.html',context)

def employee_view(request,pk):
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        employee = None
    context = {'employee':employee}
    return render(request,'userapp/employee_view.html',context)

def employee_update(request,pk):
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return redirect('employee_listing')
    form = EmployeeForm(instance = employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_listing')
    else:
        context = {'form':form}
        return render(request,'userapp/employee-form.html',context)

def employee_delete(request,pk):
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return redirect('employee_listing')
    if employee:
        employee.delete()
        return redirect('employee_listing')