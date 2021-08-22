from students.converters import FourDigitYearConverter
from django.urls import path, register_converter

from . import views

register_converter(FourDigitYearConverter, 'batky')

app_name = 'student'
urlpatterns = [
    path('', views.index, name='index'), #students/
    path('<int:student_id>', views.show, name='show'), #students/
    path('get-by-name/<slug:duongDan>/<int:student_id>', views.showBySlug, name='show-by-slug'), #students/
    path('class/<int:id>/students/name/<str:name>', views.getStudentByClass, name='student-in-class'), #students/
    path('search-by-year/<batky:year>', views.getStudentByYear, name='student-in-class-by-year'), #students/
    path('search-by-year/<str:name>', views.getStudentByName, name='student-in-class-by-name'), #students/
    path('welcome', views.welcome, name='welcome'), #students/welcome
    path('export', views.export, name='export'), #students/welcome
]

# /student/7

# <a href="/student/chi-tiet/id">Chi tiet sinh vien</a>
# <a href="/student/chi-tiet/id">Chi tiet sinh vien</a>
# <a href="/student/chi-tiet/id">Chi tiet sinh vien</a>