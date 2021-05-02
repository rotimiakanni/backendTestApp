from django.contrib import admin
from .models import Employees

class EmployeeesAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'age', 'join_date')
    search_fields = ('employee_id', 'first_name')

admin.site.register(Employees, EmployeeesAdmin)