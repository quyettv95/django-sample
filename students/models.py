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
    U = 2, 'Không xác định'


class Skill(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    class_model = models.ForeignKey(ClassModel, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, help_text="Tên sinh viên, ví dụ:  Nguyễn Văn A")
    gender = models.IntegerField(choices=GenderChoices.choices)
    address = models.TextField()
    student_code = models.CharField(max_length=200)
    is_paid = models.BooleanField(default=False)
    go_to_school_at = models.DateField(null=True)
    skills = models.ManyToManyField(Skill, verbose_name="Danh sách Kỹ năng")
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
        return self.get_gender_display()
    #anotation
    @admin.display(
        description='Kỹ năng',
    )
    def skillStr(self):
        if self.skills.count() > 0:
            skills = []
            for skill in self.skills.all():
                skills.append(str(skill))
            return ", ".join(skills)
        else:
            return "Không có kỹ năng"


    def __str__(self) -> str:
        return self.name
