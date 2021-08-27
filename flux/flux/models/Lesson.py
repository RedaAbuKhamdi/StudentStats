from django.db.models import *
from flux.models.Teacher import Teacher
from flux.models.Student import Student

class Lesson(Model):
    date = DateField()
    teacher = ForeignKey(Teacher, on_delete= CASCADE)
    students = ManyToManyField(Student)
