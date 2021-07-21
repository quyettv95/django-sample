from django.db import models
from django.contrib import admin

class ClassModel(models.Model):
    name = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class GenderChoices(models.IntegerChoices):
    S = 0, 'Nữ'
    F = 1, 'Nam'

class Student(models.Model):
    class_model = models.ForeignKey(ClassModel, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    gender = models.IntegerField(choices=GenderChoices.choices)
    address = models.TextField()
    student_code = models.CharField(max_length=200)
    is_paid = models.BooleanField(default=False)
    go_to_school_at = models.DateField(null=True)

    @admin.display(
        boolean=True,
        description='Đã thanh toán?',
    )
    def isPaid(self):
        return self.is_paid

    @admin.display(
        description='Giới tính',
    )
    def genderStr(self):
        if self.gender == 1:
            return 'Nam'
        return "Nữ"

    def __str__(self) -> str:
        return self.name
