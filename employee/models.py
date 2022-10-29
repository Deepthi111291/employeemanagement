from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=120,primary_key=True)
    profile_pic=models.ImageField(upload_to="profilepics",null=True)
    employee_name=models.CharField(max_length=120)
    designation=models.CharField(max_length=120)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    experience=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.employee_name
# null=True means even if the field is not filled ,no problem
# python manage.py makemigrations    ->generate a query file in migrations
# python manage.py migrate           ->Apply changes to database
# DJANGO ORM:to interact with the database
# CRUD
# create
# retrive
# update
# delete
# shell to try orm query->python manage.py shell
# next import Employee model(model you want to interact with)->from employee.models import Employee
# creating an employee object
# pythom -m pip install pillow