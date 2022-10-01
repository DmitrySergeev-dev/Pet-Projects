from django.contrib import admin
from .models import Student, Teacher, Subject, StudentsGroup, Lesson

mymodels = [Student, Teacher, Subject, StudentsGroup, Lesson]
admin.site.register(mymodels)
# Register your models here.
