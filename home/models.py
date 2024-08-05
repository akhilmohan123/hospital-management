from django.db import models

# Create your models here.
class Departments(models.Model):
    dept_name=models.CharField(max_length=20)
    dept_description=models.TextField()
    def __str__(self):
        return self.dept_name
class Doctors(models.Model):
    doct_name=models.CharField(max_length=20)
    doct_spec=models.CharField(max_length=255)
    dept_name=models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    doct_image=models.ImageField(upload_to='doctor')
    def __str__(self):
        return self.doct_name
