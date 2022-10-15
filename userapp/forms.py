from dataclasses import field
from django.forms import ModelForm
from .models import *

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name','employee_code','designation']