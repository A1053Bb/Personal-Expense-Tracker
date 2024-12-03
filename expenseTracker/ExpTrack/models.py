from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class Employee(models.Model):
    Empid= models.IntegerField()
    name= models.CharField(max_length=25)
    address= models.CharField(max_length=100)
    salary= models.IntegerField()
    Department= models.CharField(max_length=25)
    class Meta:
        db_table="employee"
class issue(models.Model):
      Empid=models.CharField(max_length=50)
      txn_id=models.CharField(max_length=50)
      txn_date=models.DateField()
      charges=models.IntegerField(default=0)
      class Meta:
        db_table="issue"
class login(models.Model):
      emp_id=models.CharField(max_length=50)
      pwd=models.CharField(max_length=50)
      class Meta:
          db_table="login"