from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from .student_serializer import CourseSerializer,StudentSerializer
from .models import Courses
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.authentication import BasicAuthentication 
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

## Auth API ##
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


class StudentCources(ListCreateAPIView):
    queryset = Courses.objects.all().order_by('-id')
    serializer_class = CourseSerializer    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]



    
    

    