from django.urls import path

from . import views

app_name = 'student'
urlpatterns = [
    path('', views.index, name='index'), #students/
    path('<int:i>', views.show, name='show'), #students/
    path('welcome', views.welcome, name='welcome'), #students/welcome
]

# /student/7

# <a href="/student/chi-tiet/id">Chi tiet sinh vien</a>
# <a href="/student/chi-tiet/id">Chi tiet sinh vien</a>
# <a href="/student/chi-tiet/id">Chi tiet sinh vien</a>