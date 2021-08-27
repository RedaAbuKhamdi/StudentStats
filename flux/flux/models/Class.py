from flux.flux.models.Teacher import Teacher
from flux.flux.models.Course import Course
from django.db.models import *

class Class(Model):
    number = IntegerField()
    launch_date = DateField()
    course = ForeignKey(Course, on_delete=CASCADE)
    teacher = ForeignKey(Teacher, on_delete=CASCADE)
