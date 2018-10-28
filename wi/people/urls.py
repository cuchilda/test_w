from django.urls import path

from . import views

urlpatterns = [
    path('students/', views.StudentListView.as_view(), name='students'),
    path('student/<int:student_id>/', views.detail_student, name='detail_student'),
    path('teacher/<int:teacher_id>/', views.detail_teacher, name='detail_teacher'),
    path('teachers/', views.TeachersListView.as_view(), name='teachers')
]