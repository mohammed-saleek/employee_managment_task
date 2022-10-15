from enum import unique
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=50,unique=True)
    username = models.CharField(max_length=40,unique=True)
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    
    USERNAME_FIELD: 'user_email'
    # REQUIRED_FIELDS: ['username']
    
    def __str__(self):
        return self.username

class Employee(models.Model):
    employee_name = models.CharField(max_length=40)
    employee_code = models.CharField(max_length=30,unique=True)
    designation = models.CharField(max_length=25)
    salary = models.IntegerField(null=True)
    
    def __str__(self):
        return self.employee_name
    