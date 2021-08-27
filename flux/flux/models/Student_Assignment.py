from flux.flux.models.Assignment import Assignment
from django.db.models import *
from flux.models.Student import Student

class Student_Assignment(Model):
    done = BooleanField()
    due_date = DateField()
    student = ForeignKey(Student, on_delete=CASCADE)
    assignment = ForeignKey(Assignment, on_delete=CASCADE)
    