from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.PositiveIntegerField(
        validators=[MinValueValidator(0)], default=0)
