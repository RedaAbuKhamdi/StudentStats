from flux.flux.models.Class import Class
from django.db.models import *
from flux.models.Assignment import Assignment

class Student(Model):
    name = CharField(max_length=128)
    phone = CharField()
    password = CharField()
    assignments = ManyToManyField(Assignment)
    classes = ManyToManyField(Class)