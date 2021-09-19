from students.models import Product, Student
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class RandomForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=10, label="Tiêu đề", widget=forms.TextInput(attrs={
        "class": "form-control",
    }))
    file = forms.FileField(required=False, label="Đính kèm", widget=forms.FileInput(attrs={
        "class": "form-control"
    }))

class GiaiPTB2Form(forms.Form):

    def clean(self):
        cleanData = super().clean()

        a = int(cleanData.get("a"))

        print(a)
        if a < 0:
            self.add_error('a', "Số A không được là số âm")

    a = forms.CharField(required = True, label= "Nhập số a", widget=widgets.TextInput(attrs={
        "class": "form-control",
        # "required": ""
    }), error_messages={
        'required': "Không được để trống"
    })
    b = forms.CharField(required = True, label= "Nhập số b", widget=widgets.TextInput(attrs={
        "class": "form-control"
    }))
    c = forms.CharField(required = True, label= "Nhập số c", widget=widgets.TextInput(attrs={
        "class": "form-control"
    }))


class StudentForm(forms.ModelForm):
    # def clean(self):
    #     self.add_error("name", "Hihie")
    #     self.add_error("student_code", "Mã sinh viên không hợp lệ")
    #     raise ValidationError("Hello")

    class Meta:
        model = Student
        fields = [
            'class_model',
            'name',
            'gender',
            # 'address',
            'student_code',
            'is_paid',
            'go_to_school_at',
            'skills',
            'subjects',
            # 'profile',
        ]
        labels= {
            'name': "Họ tên",
            'class_model': "Chọn lớp",
            'student_code': "Mã sinh viên"
        }
        widgets = {
            'name': widgets.TextInput(
                attrs={
                    "class": 'form-control'
                },
            ),
            'gender': widgets.Select(
                attrs={
                    "class": 'form-control'
                },
            ),
            'class_model': widgets.Select(
                attrs={
                    "class": 'form-control abc'
                },
            ),
            'go_to_school_at': widgets.DateInput(
                attrs={
                    "class": 'form-control',
                    "type" : 'date'
                },
            ),
            'student_code': widgets.DateInput(
                attrs={
                    "class": 'form-control',
                },
            ),
            'subjects': widgets.SelectMultiple(
                attrs={
                    "class": 'form-control abc',
                },
            ),
            'skills': widgets.SelectMultiple(
                attrs={
                    "class": 'form-control abc',
                },
            ),
        }


class NameForm(forms.Form):
    def clean(self):
        data = super().clean()
        name = data.get("name")
        email = data.get("email")
        print(email)
        # is-invalid

        if name is None:
            # self.fields.name.widget.attrs['class'] = "form-control is-invalid"
            self.add_error("name", "Bạn không được để trống trường họ tên")

        if email is not None and "@" not in email:
            # self.fields.name.widget.attrs['class'] = "form-control is-invalid"
            self.add_error("email", "Email không hợp lệ")


    name = forms.CharField(required= True ,label="Nhập tên của bạn", widget=forms.TextInput(attrs={
        "class": 'form-control'
    }))

    email = forms.CharField(required= True ,label="Nhập email", widget=forms.TextInput(attrs={
        "class": 'form-control'
    }))
    address = forms.CharField(label="Địa chỉ", widget=forms.Textarea(attrs={
        "class": "form-control"
    }))