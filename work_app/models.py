from django.db import models


# Create your models here.
class TodoWork(models.Model):
    title = models.CharField(max_length=250)
    des = models.TextField()
    note = models.CharField(max_length=500)


class WorkDetails(models.Model):
    todo_work = models.ForeignKey(
        TodoWork, on_delete=models.CASCADE, related_name="todo_work"
    )
    details = models.TextField()
