from django.contrib import admin
from .models import Student, ClassModel, Skill, Subject, SubjectRegistration, Profile
from students import models
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    # fields = ['name', 'gender', 'address', 'student_code', 'class_model']
    fieldsets = [
        ('Thông tin sinh viên', {'fields': [ 'name', 'gender', 'address', 'student_code']}),
        ('Lớp học', {'fields': ['class_model']}),
        ('Tình trạng thanh toán', {'fields': ['is_paid']}),
        ('Ngày nhập học', {'fields': ['go_to_school_at']}),
        ('Kỹ năng', {'fields': ['skills']}),
        ('Profile', {'fields': ['profile']}),
    ]
    list_display = ('name', 'address', 'student_code', 'isPaid', 'genderStr', 'class_model', 'skillStr')
    list_filter = ['gender', 'class_model', 'is_paid', 'go_to_school_at']
    search_fields = ['name', 'address', 'student_code']

# class StudentInline(admin.StackedInline):
#     model = Student
#     extra = 2
class StudentInline(admin.TabularInline):
    model = Student
    extra = 2

class ClassAdmin(admin.ModelAdmin):
    fields = ['name', 'teacher_name']
    inlines = [StudentInline]
class SubjectRegistrationAdmin(admin.ModelAdmin):
    fields = ['student', 'subject', 'reg_at', 'score']
    list_display = ['student', 'subject', 'reg_at', 'score']
    list_filter = ['student', 'subject']
    # inlines = [StudentInline]

admin.site.register(ClassModel, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Skill)
admin.site.register(Subject)
admin.site.register(Profile)
admin.site.register(SubjectRegistration, SubjectRegistrationAdmin)
