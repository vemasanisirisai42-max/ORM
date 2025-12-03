from django.db import models
from django.contrib import admin
class Employee (models.Model):
    eid=models.CharField(primary_key=True,max_length=20)
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=["eid","name","salary","age","email"]