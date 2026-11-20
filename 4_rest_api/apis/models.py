from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    grade = models.CharField(max_length=50)
    room = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.school.abbreviation} - {self.grade}/{self.room}"

class Teacher(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers', blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"