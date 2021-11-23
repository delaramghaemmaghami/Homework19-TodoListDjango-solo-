from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=250)
    explanation = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    PRIORITY_OF_TASKS = [
        ("high", "high"),
        ("medium", "medium"),
        ("low", "low")
    ]
    priority = models.CharField(max_length=6, choices=PRIORITY_OF_TASKS, default="low")

    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.title
