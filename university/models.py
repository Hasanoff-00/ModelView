from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)

class Group(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Kafedra(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE)

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE)

