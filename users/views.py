from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.views import generic
from django.views.generic import TemplateView
from users.models import User


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=User.objects.get(email=email), password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('homepageStudent')

        else:
            messages.info(request, 'Неверные данные пользователя')
            return redirect('login')

    else:
        return render(request, 'forStudents.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        classof = request.POST['classes']
        school = request.POST['school']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Пользователь с таким Email уже существует')
                return redirect('register')
            else:
                user = User.objects.create_user(password=password1, email=email,
                                                first_name=name,last_name=surname,classof=classof,school=school)
                user.save()
                return redirect('homepageStudent')
    else:
        return render(request, 'forStudents.html')


def index(request):
    return render(request, 'index.html')


# def forStudents(request):
#     return render(request, 'forStudents.html')


def forTeachers(request):
    return render(request, 'forTeachers.html')

def homepageStudent(request):
    return render(request, 'homepage_student.html')

def books(request):
    return render(request, 'books_homepage.html')


def lessons(request):
    return render(request, 'lessons.html')

def math(request):
    return render(request, 'mat_page.html')

def exams(request):
    return render(request, 'exams.html')

def forum(request):
    return render(request, 'forum.html')

def newpost(request):
    return render(request, 'newpost.html')

def mathTema(request):
    return render(request, 'mathTema.html')

def schoolBooks(request):
    return render(request, 'schoolBooks.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import auth
# from django.views import generic
# from django.views.generic import TemplateView
# from users.models import User
#
#
# class LoginView(TemplateView):
#     template_name = 'login.html'
#
#     def post(self, request, *args, **kwargs):
#         email = request.POST['email']
#         password = request.POST['password']
#         user = auth.authenticate(username=User.objects.get(email=email), password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.info(request, 'Неверные данные пользователя')
#             return render(request, self.template_name)
#
#
# def register(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         if password:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Пользователь с таким Email уже существует')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(password=password, email=email,
#                                                 first_name=name)
#                 user.save()
#                 return redirect('login')
#     else:
#         return render(request, 'registration.html')
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
#
