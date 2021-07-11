from django.db import models

# Create your models here.
class personal(models.Model):
    name = models.CharField(max_length=100,null='True')
    Gender = models.CharField(max_length=12,null='True')
    Worktype= models.CharField(max_length=20,null='True')
    Foodhabit = models.CharField(max_length=30,null='True')
    Height = models.IntegerField(null='True')
    Weight = models.IntegerField(null='True')
    Glucose=models.CharField(max_length=100,null='True')
    BloodPressure=models.CharField(max_length=100,null='True')
    Pailor = models.CharField(max_length=5,null='True')
    Bitotsspot = models.CharField(max_length=5,null='True')
    Goitre = models.CharField(max_length=5,null='True')
    Pittingodema = models.CharField(max_length=5,null='True')
    Breakfast = models.CharField(max_length=100,null='True')
    Lunch = models.CharField(max_length=100,null='True')
    Snack = models.CharField(max_length=100,null='True')
    Dinner = models.CharField(max_length=100,null='True')

class Diet(models.Model):
    Nameofthediet = models.CharField(max_length=50)
    DietImage=models.ImageField(upload_to="pics")

class Food(models.Model):
    Nameofthefood = models.CharField(max_length=50)
    Calories = models.CharField(max_length=50)
    Carbs = models.CharField(max_length=50)
    Protein = models.CharField(max_length=50)
    Fat = models.CharField(max_length=50)

class Contact (models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Query = models.TextField()

