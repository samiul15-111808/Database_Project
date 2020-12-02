from django.shortcuts import render,redirect
from main.models import *
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html')


def student(request):
    if request.method == "GET":
        student = Student.objects.all()
        context = {
            'student': student
        }
        return render(request, 'main/student.html', context)
    elif request.method == "POST":
        name = request.POST["name"]
        varsity_id = request.POST["varsity_id"]
        email = request.POST["email"]
        cgpa = request.POST["cgpa"]

        Student.objects.create(name=name, varsity_id=varsity_id,email=email, cgpa=cgpa )
        return redirect('/student')


def student_action(request,action,id):
    if action == "Delete":

        student = Student.objects.get(id=id)

        student.delete()
    elif action == "Edit":
        if request.method == "GET":
            student = Student.objects.get(id=id)
            context = {
                'student': student
            }
            return render(request, 'main/student_edit.html',context)
        elif request.method == "POST":
            input_name = request.POST["name"]
            input_email = request.POST["email"]
            input_id = request.POST["id"]
            input_cgpa = request.POST["cgpa"]

            student = Student.objects.get(id=id)

            student.name = input_name
            student.email = input_email
            student.varsity_id = input_id
            student.cgpa = input_cgpa
            student.save()
    return redirect('/student')


def teacher(request):
    if request.method == "GET":
        teacher = Teacher.objects.all()
        context = {
            'teacher': teacher
        }
        return render(request, 'main/teacher.html', context)

    elif request.method == "POST":
        name = request.POST["name"]
        courses = request.POST["course"]

        Teacher.objects.create(name=name, course=courses)
        return redirect('/teacher')


def teacher_action(request, action, tid):
    if action == "delete":
        teacher = Teacher.objects.get(id=tid)
        teacher.delete()

    elif action == "Edit":
        if request.method == "GET":
            teacher = Teacher.objects.get(id=tid)

            context = {
                'teacher': teacher
            }
            return render(request, 'main/teacher_edit.html', context)
        elif request.method == "POST":
            input_name = request.POST["name"]
            input_course = request.POST["course"]

            teacher = Teacher.objects.get(id=tid)
            teacher.name = input_name
            teacher.course =input_course

            teacher.save()

    return redirect("/teacher")





def course(request):
    if request.method == "GET":
        course = Courses.objects.all()
        context = {
            'course': course
        }
        return render(request, 'main/courses.html', context)
    elif request.method == "POST":
        course_name = request.POST["name"]
        course_code = request.POST['course']


        Courses.objects.create(course_name=course_name, course_code=course_code)
        return redirect('/course')

def course_action(request, action, id):
    if action == "Delete":
        course = Courses.objects.get(id=id)
        course.delete()
    elif action =="Edit":
        if request.method =="GET":
            course = Courses.objects.get(id=id)
            context = {
                'course': course
            }
            return render(request, 'main/course_edit.html', context)
        elif request.method == "POST":
            input_courseName = request.POST["name"]
            input_courseCode = request.POST["course"]

            course = Courses.objects.get(id=id)
            course.course_name = input_courseName
            course.course_code = input_courseCode
            course.save()

    return redirect("/course")









