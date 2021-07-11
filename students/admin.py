from django.contrib import admin
from .models import Student, ClassModel
# Register your models here.

admin.site.register(ClassModel)
admin.site.register(Student)
