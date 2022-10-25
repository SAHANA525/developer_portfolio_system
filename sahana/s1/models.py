from django.db import connections
from django.db import models

# Create your models here.

class Admin(models.Model):   
    username= models.CharField(max_length=500)
    password= models.CharField(max_length=1000)
    class Meta:
        db_table = "admin"

class Student(models.Model):   
    phone= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    title= models.CharField(max_length=100)
    role= models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    class Meta:
        db_table = "students"

class Skill(models.Model):   
    skill= models.CharField(max_length=500)
    description= models.CharField(max_length=1000)
    class Meta:
        db_table = "skills"

class Project(models.Model):   
    project= models.CharField(max_length=500)
    description= models.CharField(max_length=1000)
    class Meta:
        db_table = "projects"

class Eduction(models.Model):   
    degree= models.CharField(max_length=500)
    specialization= models.CharField(max_length=500)
    university= models.CharField(max_length=500)
    school= models.CharField(max_length=500)
    yop= models.CharField(max_length=500)
    per= models.CharField(max_length=500)
    class Meta:
        db_table = "eduction"

class Experience(models.Model):   
    company= models.CharField(max_length=500)
    role= models.CharField(max_length=500)
    nyear= models.CharField(max_length=500)
    description= models.CharField(max_length=1000)
    class Meta:
        db_table = "experience"

class Intrests(models.Model):   
    hobies= models.CharField(max_length=500)
    links= models.CharField(max_length=1000)
    class Meta:
        db_table = "intrests"


