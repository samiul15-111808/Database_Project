from django.db import models

class Student(models.Model):
    varsity_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    cgpa = models.CharField(max_length=20)

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)

class Courses(models.Model):
    course_name = models.CharField(max_length=20)
    course_code = models.IntegerField()