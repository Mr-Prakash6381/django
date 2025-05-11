from django.db import models

class Student(models.Model):
    Student_id=models.IntegerField(default=0)
    Student_Name=models.CharField(max_length=50,null=True)
    Student_Course=models.CharField(max_length=50,null=True)
    Student_Deprt=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.Student_Name
