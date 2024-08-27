from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField("Name",max_length=60)
    email =models.EmailField()
    document = models.CharField("Document",max_length=20)
    phone = models.CharField(max_length=20)
    registration_date = models.DateField("Registration Date", auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.id}. {self.name}"
    
    