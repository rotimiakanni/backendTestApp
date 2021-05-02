from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
import json

# Create your views here.
Accounts = get_user_model()

@api_view(["POST"])
@permission_classes((AllowAny,))
def signup_view(request):
    payload = request.data
    try:
        email = payload['email'].lower()
        password = payload['password']
    except:
        return Response({'message':'please enter signup credentials'}, status=400)
    try:
        check_user = Accounts.objects.get(email=email)
        if check_user and check_user.is_active:
            response = {
                'message': 'Email already registered.'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
    except Accounts.DoesNotExist:
        user = Accounts.objects.create_user(
            email=email, password=password)
        return Response({'message':'User successfully created.'}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes((AllowAny,))
def login_view(request):
    payload = json.loads(request.body)
    email = payload["email"].lower()
    password = payload["password"]
    if email is None or password is None:
        return Response({'error': 'Please provide both email and password'},
                        status=400)
    user = authenticate(email=email, password=password)
    if not user:
        response = {'message': 'Please sign up or check your credentials again.'}
        return Response(response, status=400)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)