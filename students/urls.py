from os import name
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
    path('test-form', views.testForm), #Home page/
    path('test-form-edit/<int:id>', views.testFormEdit), #Home page/
    path('test-session', views.testSession), #Home page/
    path('form-giai-pt-b2', views.giaiPtB2), #Home page/
    path('add-to-cart', views.addToCart), #Home page/
    path('cart', views.viewCart), #Home page/
    path('clear-cart', views.clearCart), #Home page/
    path('delete-cart-item/<int:product_id>', views.deleteCartItem, name="delete-cart-item"), #Home page/
    path('update-quantity/<int:product_id>', views.updateQuantity, name="update-cart-item"), #Home page/
    path('show-form-name', views.showFormName), #
]

# /student/7

# <a href="/student/chi-tiet/id">Chi tiet sinh vien</a>
# <a href="/student/chi-tiet/id">Chi tiet sinh vien</a>
# <a href="/student/chi-tiet/id">Chi tiet sinh vien</a>