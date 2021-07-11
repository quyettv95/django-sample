from django.db import models

class ClassModel(models.Model):
    name = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    class_model = models.ForeignKey(ClassModel, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    gender = models.IntegerField()
    address = models.TextField()
    student_code = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
