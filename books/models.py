from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=256)
    users = models.ManyToManyField(User, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, unique_with='id')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    file = models.FileField(upload_to="book/%y")

    class Meta:
        verbose_name = 'Китеп'
        verbose_name_plural = 'Китептер'

    def __str__(self):
        return self.caption
