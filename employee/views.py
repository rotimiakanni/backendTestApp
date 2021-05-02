from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.conf import settings
from rest_framework import viewsets
from .paginator import CustomPagination
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
# from django.contrib.auth.signals import user_logged_in
import json

from rest_framework import status
from .models import Employees
from .serializers import EmployeeSerializer

from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated


class EmployeesView(ListCreateAPIView):
    """clas type view to handle the todo on the individual dahsboard"""
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomPagination

    def get_queryset(self):
        all_employees = Employees.objects.get_queryset().order_by('id')
        return all_employees

@api_view(["PUT"])
def update_employee(request, employee_id):
    try:
        employee = Employees.objects.get(employee_id=employee_id)
    except Employees.DoesNotExist:
        return Response({'message':'Employee does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'message':'update successful'}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_employee(request):
    if request.method == 'POST':
        employee = Employees()
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'message':'Employee Successfully created'}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_employee(self, employee_id):
    try:
        employee = Employees.objects.get(employee_id=employee_id)
        employee.delete()
        return Response({'message':'Successful'}, status=status.HTTP_200_OK)
    except Employees.DoesNotExist:
        return Response({'message':'Employee does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def get_employee(request, employee_id):
    try:
        employee = Employees.objects.get(employee_id=employee_id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Employees.DoesNotExist:
        return Response({'message':'Employee does not exist'}, status=status.HTTP_404_NOT_FOUND)