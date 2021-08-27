from django.db.models import *

class Course(Model):
    course_name = CharField(128)