from django.urls import path

from books.views import DashboardView

urlpatterns = [

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
