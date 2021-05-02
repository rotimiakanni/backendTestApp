from django.db import models


class Employees(models.Model):    
    employee_id = models.CharField(max_length=6, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    join_date = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name

