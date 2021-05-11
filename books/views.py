from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Book, Category


class DashboardView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'categories': Category.objects.filter(users=request.user),
            'courses': Book.objects.filter(category__users=request.user)
        }
        return render(request, self.template_name, context)

