from django.db import models

# Employee model
class Employee(models.Model):
    # Foreign key to be used appropriately in related tables, not within itself
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    expense = models.IntegerField()
    income = models.IntegerField()  # Replacing salary with income and expense
    department = models.CharField(max_length=25)

    class Meta:
        db_table = "employee"

# Login model
class login(models.Model):
    firstname = models.CharField(max_length=50)  # First name of the user
    lastname = models.CharField(max_length=50)  # Last name of the user
    emp_id = models.CharField(max_length=50, unique=True, primary_key=True)  # Employee ID as the primary key
    pwd = models.CharField(max_length=50)  # Password field

    class Meta:
        db_table = "login"

# Issue model
class Issue(models.Model):
    emp_i = models.ForeignKey(login, on_delete=models.CASCADE, related_name='issues')  # Proper ForeignKey relation to Employee
    txn_id = models.CharField(max_length=50, unique=True, primary_key=True)  # Unique transaction ID
    txn_name = models.CharField(max_length=100)
    txn_date = models.DateField()
    charges = models.IntegerField(default=0)
    txn_type = models.CharField(max_length=20,default="Undefined")

    class Meta:
        db_table = "issue"

# Category model
class Category(models.Model):
    emp_c = models.ForeignKey(login, on_delete=models.CASCADE, related_name="categories")
    category_name = models.CharField(max_length=100)  # Name of the category
    category_amount = models.IntegerField(default=0)  # Amount associated with the category

    class Meta:
        db_table = "category"
