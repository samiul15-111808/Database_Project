
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('student/', views.student),
    path('teacher/', views.teacher),
    path('course/', views.course),
    path('student/<str:action>/<str:id>/', views.student_action),
    path('teacher/<str:action>/<str:tid>/', views.teacher_action),
    path('course/<str:action>/<str:id>/', views.course_action)



]
