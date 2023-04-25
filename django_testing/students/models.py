from django.db import models


class Student(models.Model):
    name = models.TextField()

    birth_date = models.DateField(
        null=True,
    )

    def __str__(self):
        return f"Student name - {self.name}"


class Course(models.Model):
    name = models.TextField()

    students = models.ManyToManyField(
        Student,
        blank=True,
    )

    def __str__(self):
        students = list(self.students.values('name'))
        return f"Course name - {self.name} students - {students}"
