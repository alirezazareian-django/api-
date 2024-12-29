from django.db import models

class Student(models.Model):
    Name=models.CharField(max_length=20)
    Family=models.CharField(max_length=20)
    Code=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return super().__str__()
