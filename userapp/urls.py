from django.urls import path,include
from . import views
urlpatterns = [
    path('login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('add_employee',views.add_employee,name='add_employee'),
    path('employee_listing',views.employee_listing,name='employee_listing'),
    path('add_salary',views.add_salary,name='add_salary'),
    path('employee_view/<int:pk>',views.employee_view,name='employee_view'),
    path('employee_update/<int:pk>',views.employee_update,name='employee_update'),
    path('employee_delete/<int:pk>',views.employee_delete,name='employee_delete'),
]