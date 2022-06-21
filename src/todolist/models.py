from django.db import models
from django.utils.text import slugify


# Create your models here.

class ListElements(models.Model):
    element = models.CharField(blank=False, max_length=500)
    deadLine = models.DateField(blank=True, null=True)
    reminder = models.BooleanField(default=False)
    mark_as_done = models.BooleanField(default=False)
    listId = models.ForeignKey('TodoList', on_delete=models.CASCADE)

    def __str__(self):
        return self.element


class TodoList(models.Model):
    title = models.CharField(max_length=225, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    author = models.EmailField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

