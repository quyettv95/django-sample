import students
from django.db import models
from django.contrib import admin
from django.db.models.base import Model
from django.urls import reverse


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


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    id_code = models.CharField(null=True, max_length=255, unique=True)
    dob = models.DateField(null=True)
    phone = models.CharField(null=True, max_length=255)

    def __str__(self):
        return self.id_code + str(self.dob) + self.phone

class Student(models.Model):
    class Meta:
        permissions = [
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
            ("grade_latest_exam_score", "Cập nhật điểm đồ án tốt nghiệp"),
        ]
    id = models.BigAutoField(primary_key=True)
    class_model = models.ForeignKey(ClassModel, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, help_text="Tên sinh viên, ví dụ:  Nguyễn Văn A")
    gender = models.IntegerField(choices=GenderChoices.choices)
    address = models.TextField()
    student_code = models.CharField(max_length=200)
    is_paid = models.BooleanField(default=False)
    go_to_school_at = models.DateField(null=True)
    skills = models.ManyToManyField(Skill, verbose_name="Danh sách Kỹ năng")
    subjects = models.ManyToManyField(Subject, through='SubjectRegistration')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    @admin.display(
        boolean=True,
        description='Đã thanh toán?',
    )
    def isPaid(self):
        return self.is_paid

    def get_absolute_url(self):
        student_id = self.id
        return reverse('student:show', args=(student_id,))

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

class SubjectRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Sinh viên")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Môn học")
    reg_at = models.DateField(null=True, verbose_name="Ngày đăng ký")
    score = models.FloatField(default=0, verbose_name="Điểm trung bình")

    def __str__(self):
        return str(self.student) + " - " + str(self.subject)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="products")

    def __str__(self):
        return "[" + str(self.id) + "] " + self.name


class Order(models.Model):
    def __str__(self) -> str:
        return self.customer_name

    customer_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    total = models.IntegerField(default=0)

class OrderDetail(models.Model):
    product = models.ForeignKey(Product, verbose_name="Sản phẩm", on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, verbose_name="Đơn hàng", on_delete=models.CASCADE)
