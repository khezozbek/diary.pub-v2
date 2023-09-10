from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    TYPE_CHOICES = [
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
        ('Parent', 'Parent'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    groups = models.ManyToManyField('Group')


class Group(models.Model):
    name = models.CharField(max_length=50)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    level = models.CharField(max_length=50)


class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_results')
    month = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    comment = models.TextField()


class ScoreHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='score_history')
    month = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=3, decimal_places=1)


class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
