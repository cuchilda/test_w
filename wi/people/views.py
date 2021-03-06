from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.generic.list import ListView
from .scripts.generate_users import generate_students, generate_teachers


from people.models import Teacher, Student

def students_list(request):
    latest_students = Student.objects.order_by('-entry_date')[:5]
    template = loader.get_template('people/teacher_list.html')
    context = {'latest_student' : latest_students}
    return HttpResponse(template.render(context, request))

def detail_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404('El estudiante consultado no existe')
    return render(request, 'people/detail_student.html', {'student':student})

def teachers_list(request):
    latest_teachers = Student.objects.order_by('-entry_date')[:5]
    template = loader.get_template('people/teacher_list.html')
    context = {'latest_student' : latest_teachers}
    return HttpResponse(template.render(context, request))

def detail_teacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
    except Teacher.DoesNotExist:
        raise Http404('El profesor consultado no existe')
    return render(request, 'people/detail_teacher.html', {'teacher':teacher})

def generator_students(request, n_students):
    generate_students(n_students)
    return HttpResponse("%s estudiantes han sido generados" % n_students)

def generator_teachers(request, n_teachers):
    generate_teachers(n_teachers)
    return HttpResponse("%s profesoras han sido generadas" % n_teachers)

class TeachersListView(ListView):
    model = Teacher
    paginate_by = 8

class StudentListView(ListView):
    model = Student
    paginate_by = 8