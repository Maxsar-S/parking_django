from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    EMPLOYEE = 'E'
    MANAGER = 'M'
    position_choices = (
        (EMPLOYEE, 'Employee'),
        (MANAGER, 'Manager'),
    )
    position = models.CharField(max_length=1,
                                choices=position_choices,
                                default=EMPLOYEE)


class Space(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

