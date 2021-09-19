import students
from students.form import RandomForm, StudentForm, GiaiPTB2Form, NameForm
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product, Student, SubjectRegistration
from django.template.defaultfilters import slugify
from django.urls import reverse
import csv
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    # print(request.scheme)
    # print(request.method)
    # print(request.path)
    # print(request.path_info)
    hoten  = request.POST.get('hoten', '')
    # print(request.GET.get('tuoi'))
    # print(request.COOKIES.get('username'))
    # print(request.FILES.get('image'))
    students = Student.objects.filter(name__icontains=hoten)
    data = {
        'students': students,
        'hoten': hoten,
        'genderMeta': {
            1: "Nam",
            2: "Nữ",
        }
    }

    return render(request, 'students/index.html', data)

def show(request, student_id):

    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Sinh viên không tồn tại")
    subjectRegistrations = SubjectRegistration.objects.filter(student=student)
    slugGenerate = slugify(student.name)
    print(slugGenerate)
    data = {
        "student": student,
        "subjectRegistrations": subjectRegistrations,
    }
    print(subjectRegistrations)
    return render(request, 'students/show.html', data)

def showBySlug(request, duongDan, student_id):
    # print(slug)
    student = Student.objects.get(pk=student_id)
    subjectRegistrations = SubjectRegistration.objects.filter(student=student)
    slugGenerate = slugify(student.name)
    print(slugGenerate)
    data = {
        "student": student,
        "subjectRegistrations": subjectRegistrations,
    }
    print(subjectRegistrations)
    return render(request, 'students/show.html', data)

def getStudentByClass(request, id, name):
    print(id)
    print(name)

    return HttpResponse("Danh sách sinh viên của lớp có id " + str(id) + " có tên " + name)
    # return render(request, 'students/show.html', data)

def getStudentByYear(request, year):
    print(year)

    return HttpResponse("Danh sách sinh viên của có năm sinh" + str(year))
    # return render(request, 'students/show.html', data)

def getStudentByName(request, name):

    return HttpResponse("Danh sách sinh viên có tên " + name)
    # return render(request, 'students/show.html', data)

def welcome(request):
    # Solution 1
    # std = Student.objects.get(pk=1)
    # return redirect(std)

    # Solution 2
    return redirect(reverse('student:show', args=(10,)))


    # Solution 3
    return redirect("https://google.com")

    year = 1995
    url = reverse('student:student-in-class-by-year', args=(year,))
    name = "Quyet Quyet2"
    url = reverse('student:student-in-class-by-name', args=(name,))
    return HttpResponse(url)



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def export(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="students.csv"'},
    )

    writer = csv.writer(response)
    students = Student.objects.all()
    for std in students:
        writer.writerow([std.id, std.name, std.gender, std.address])

    # return

def testForm(request):
    f = StudentForm()

    if request.method == "POST":
        f = StudentForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse('Success')
    else:
        f = StudentForm()

    response = render(request, 'students/test-form.html', {"f": f})
    return response

def testFormEdit(request, id):
    f = StudentForm()
    students = Student.objects.get(pk=id)
    print(students)
    # print(request.session.items())
    if request.method == "POST":
        f = StudentForm(request.POST, instance= students)
        print(f.errors.as_data().get("1221"))
        if f.is_valid():
            f.save()
            return HttpResponse('Success')
    else:
        f = StudentForm(instance=students)


    response = render(request, 'students/test-form.html', {"f": f})
    return response


def testSession(request):
    # print(request.COOKIES)
    request.session['cart'] = [
        {
            "name" : "Iphone 12",
            "price": 1000,
            "quantity": 2
        }
    ]

    return HttpResponse("Test Session")


def addToCart(request):
    # print(request.COOKIES)
    product = Product.objects.get(pk=1)
    cart = []
    if "cart" in request.session:
        cart = request.session['cart']
    updatedCart = []
    inCart = False
    for cartProduct in cart:
        currentId = cartProduct.get('id')
        if currentId == product.id:
            inCart = True
            cartProduct['quantity'] = cartProduct['quantity'] + 1
        updatedCart.append(cartProduct)

    if inCart == False:
        updatedCart.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': 1,
        })


    request.session['cart'] = updatedCart

    # return HttpResponse('Add to cart')
    return HttpResponseRedirect('/sinhvien/cart')

def clearCart(request):
    del request.session['cart']
    return HttpResponse("Xóa sạch giỏ hàng")

def updateQuantity(request, product_id):
    # del request.session['cart']
    quantity = request.POST['quantity']


    product = Product.objects.get(pk=product_id)
    cart = []
    if "cart" in request.session:
        cart = request.session['cart']
    updatedCart = []
    inCart = False
    for cartProduct in cart:
        currentId = cartProduct.get('id')
        if currentId == product.id:
            inCart = True
            cartProduct['quantity'] = quantity
        updatedCart.append(cartProduct)

    if inCart == False:
        updatedCart.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': product_id,
        })


    request.session['cart'] = updatedCart
    return HttpResponseRedirect('/sinhvien/cart')

    # return HttpResponse("Cập nhật số lượng giỏ hàng")

def viewCart(request):
    cart = None
    if "cart" in request.session:
        cart = request.session['cart']
    print(cart)
    return render(request, 'cart.html', {"cart": cart})

def deleteCartItem(request, product_id):

    cart = []
    if "cart" in request.session:
        cart = request.session['cart']
    updatedCart = []
    for cartProduct in cart:
        currentId = cartProduct.get('id')
        if currentId != product_id:
            updatedCart.append(cartProduct)

    request.session['cart'] = updatedCart

    return HttpResponseRedirect('/sinhvien/cart')

    # return HttpResponse("Xóa sản phẩm trong giỏ hàng")



def giaiPtB2(request):
    f = GiaiPTB2Form()
    if request.method == "POST":
        f = GiaiPTB2Form(request.POST)
        if f.is_valid():
            a = f.cleaned_data.get("a")
            b = f.cleaned_data.get("b")
            c = f.cleaned_data.get("c")
            print(a)
            print(b)
            print(c)
    return render(request, 'students/test-form.html', {
        'f': f
    })


def showFormName(request):
    form = NameForm()
    if request.method == "POST":
        # c1
        # name = request.POST.get("name")
        # return HttpResponse("Hello" + name)

        # c2
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            address = form.cleaned_data.get("address")
            return HttpResponse("Hello:" + name + " Address:" + address)
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'


    return render(request, 'form-demo.html', {'form': form})