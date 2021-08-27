from django.db.models import *

class Assignment(Model):
    name = CharField()
    content = CharField()