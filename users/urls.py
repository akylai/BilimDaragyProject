from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forTeachers/', views.forTeachers, name='forTeachers'),
    path('register/', views.register, name='register'),
    path('register/register', views.register, name='register'),
    path('register/login', views.login, name='register'),
    path('login/', views.login, name='login'),
    path('homepageStudent/',views.homepageStudent,name='homepageStudent'),
    path('books/',views.books,name='books'),
    path('schoolBooks/', views.schoolBooks, name='schoolBooks'),
    path('lessons/', views.lessons, name='lessons'),
    path('math/', views.math, name='math'),
    path('exams/', views.exams, name='exams'),
    path('forum/', views.forum, name='forum'),

    path('newpost/', views.newpost, name='newpost'),
    path('mathTema/', views.mathTema, name='mathTema'),
    path('logout/', views.logout, name='logout'),


]
