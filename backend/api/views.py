from django.http import response
from django.shortcuts import render
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def getAllCourses(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudentProfile(request):
    user = request.user
    student = Student.objects.get(user=user)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)