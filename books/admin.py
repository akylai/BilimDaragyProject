from django.contrib import admin
from .models import Category, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (BookInline,)
