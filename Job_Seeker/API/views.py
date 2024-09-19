from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Job,Profile,Application
from .serializers import JobSerializer,ProfileSerializer,ApplicationSerializer,UserSerializer
from rest_framework.permissions import BasePermission,IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class IsAuthenticatedOrRedirect(BasePermission):
    """
    Custom permission class to check if the user is authenticated.
    Redirect to login if not authenticated.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# (admin/employer only)
class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# (admin/employer only)
class JobUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]


class ApplyForJobView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticatedOrRedirect]

class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

        return Response({"error": "Invalid credentials"}, status=400)