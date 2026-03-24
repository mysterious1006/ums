from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    hod_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=100)   # B.Tech CSE
    duration_years = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    semester = models.IntegerField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name