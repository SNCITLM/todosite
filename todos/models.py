from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Todo(models.Model):
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default = False)
    progress = models.PositiveIntegerField(default=0,
        validators=[
            MaxValueValidator(100)
        ])

    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        status = 'V' if self.completed else 'X'
        return status + ': ' + self.description
