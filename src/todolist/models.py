from django.db import models
from django.utils.text import slugify


# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=225, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    author = models.EmailField(blank=True, null=True)
    elements = models.JSONField(blank=True, null=True)

    # {
    #     "text": {
    #         "before": "date",
    #         "reminder": "bool",
    #         "done": "bool"
    #     },
    #     "text2": {
    #         "before": "date",
    #         "reminder": "bool",
    #         "done": "bool"
    #     }
    # }

    def __str__(self):
        return self.title

