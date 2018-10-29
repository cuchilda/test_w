from random import randint
from people.models import Teacher, Student

namesfile = open("people/scripts/namesf.txt").readlines()
surnamesfile = open("people/scripts/surnames.txt").readlines()


def generate_teachers(number=1):
    for x in range(0, number):
        name = namesfile[randint(0, len(namesfile)-1)]
        surname = surnamesfile[randint(0, len(surnamesfile)-1)]
        t = Teacher(name=name, surname=surname,
                    type=Teacher.TEACHER_CHOICES[randint(0, len(list(Teacher.TEACHER_CHOICES))-1)][1],
                    email="{}.{}.teacher@wischool.com".format(name, surname),
                    active_user = randint(0,1)
                )
        t.save()


def generate_students(number=1):
    if not Teacher.objects.all():
        print("There are not student, please add teachers")
    teachers = [x.id for x in Teacher.objects.all()]
    for x in range(0, number):
        name = namesfile[randint(0, len(namesfile)-1)]
        surname = surnamesfile[randint(0, len(surnamesfile)-1)]
        s = Student(name=name, surname=surname,
                    type=Student.STUDENT_CHOICES[randint(0, len(list(Student.STUDENT_CHOICES)) - 1)][1],
                    email="{}.{}.student@wischool.com".format(name, surname),
                    active_user=randint(0, 1),
                    teacher=Teacher.objects.filter(id=teachers[randint(0, len(teachers)-1)])[0]
                    )
        s.save()

# generate_teachers(10)
# generate_students(50)
