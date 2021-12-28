from django.urls import path
from django.urls import path
from .views import getAllCourses, getStudentProfile

urlpatterns = [
    path('', getAllCourses, name="course_list"),
    path('student/', getStudentProfile, name="user_profile"),
]