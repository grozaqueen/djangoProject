from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    PRIORITY_CHOICES = (
        (1, 'Очень низкий приоритет'),
        (2, 'Низкий приоритет'),
        (3, 'Средний приоритет'),
        (4, 'Высокий приоритет'),
        (5, 'Очень высокий приоритет'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='New')
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    PRIORITY_CHOICES = (
        (1, 'Очень низкий приоритет'),
        (2, 'Низкий приоритет'),
        (3, 'Средний приоритет'),
        (4, 'Высокий приоритет'),
        (5, 'Очень высокий приоритет'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)