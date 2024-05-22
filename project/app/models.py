from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=300)
    Email=models.EmailField()
    Password=models.CharField(max_length=300)


    class Meta:
        db_table='Employee'
        verbose_name_plural='Employee'
    def __str__(self):
        return self.Name
    
class Query(models.Model):
    Query=models.CharField(max_length=300)
    Discriptions=models.CharField(max_length=300)
    Email=models.EmailField()
