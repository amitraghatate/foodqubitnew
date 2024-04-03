from django.db import models
import uuid

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    medical_condition = models.TextField(blank=True, null=True)
    food_habit = models.TextField(blank=True, null=True)
    food_allergies = models.TextField(blank=True, null=True)
    meal_day = models.TextField(blank=True, null=True)
    junk_food = models.TextField(blank=True, null=True)
    breakfast = models.TextField(blank=True, null=True)
    lunch = models.TextField(blank=True, null=True)
    snacks = models.TextField(blank=True, null=True)
    dinner = models.TextField(blank=True, null=True)
    workout = models.TextField(blank=True, null=True)
    active_day = models.TextField(blank=True, null=True)
    api_key = models.CharField(max_length=40, unique=True, default=str(uuid.uuid4())[:40])

    def __str__(self):
        return f"{self.name} - {self.email}"

class adminPanel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='myapp/images/')

"""
from django.db import models
from django.contrib.auth.models import User

'''
class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    current_weight = models.FloatField()
    current_height = models.FloatField()
    bmi = models.FloatField()
    education_details = models.TextField()

    def __str__(self):
        return self.email
    '''

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=255, default='DEFAULT VALUE')
    email = models.EmailField()
    password = models.CharField(max_length=255, default='DEFAULT VALUE')
    name = models.CharField(max_length=255, default='DEFAULT VALUE')
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default='0')
    current_weight = models.CharField(max_length=255, default='0')
    current_height = models.CharField(max_length=255, default='0')
    bmi = models.CharField(max_length=255, default='0')
    education_details = models.CharField(max_length=255, default='DEFAULT VALUE')
    occupation = models.CharField(max_length=255, default='DEFAULT VALUE')
    medical_condition = models.CharField(max_length=255, default='DEFAULT VALUE')

    def __str__(self):
        return self.phone_number
        """

