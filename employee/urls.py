from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('get-all-employees', views.EmployeesView.as_view()),
    path('get-employee/<employee_id>', views.get_employee),
    path('delete-employee/<employee_id>', views.delete_employee),
    path('create-employee/', views.create_employee),
    path('update-employee/<employee_id>/', views.update_employee),
]
