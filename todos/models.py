from django.db import models


class Todo(models.Model):
    description = models.CharField(max_length=100)
    completed = models.BooleanField()

    def __str__(self):
        status = 'V' if self.completed else 'X'
        return status + ': ' + self.description
