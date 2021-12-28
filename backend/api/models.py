from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import F
from django.db.models.fields.related import OneToOneField
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    code = models.CharField(max_length=256, blank=False, null=False)
    unit = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.code

class Faculty(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    
    def __str__(self) :
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programme(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    course_id = models.ManyToManyField(Course)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256, blank=False, null=False)
    last_name = models.CharField(max_length=256, blank=False, null=False)
    email = models.EmailField(max_length=256, blank=False, null=False)
    matric_number = models.CharField(max_length=256, blank=False, null=False)
    programme_id = models.ForeignKey(Programme, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

