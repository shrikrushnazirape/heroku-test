from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=120)
    roll_no = models.CharField(max_length = 6)
    certi = models.ImageField()
    

    def __str__(self):
        return self.name
    