from django.db.models import *

class Teacher(Model):
    name = CharField(max_length=128)
    email = CharField(max_length=128)
    password = CharField()
    phone_number = CharField()