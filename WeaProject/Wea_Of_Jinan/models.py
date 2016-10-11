from django.db import models

# Create your models here.
class Detail(models.Model):
    Feels_Like = models.CharField(max_length=20)
    Current_Temp = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

class DayTime_Weather(models.Model):
    Top_Temp = models.CharField(max_length=20)
    DTWea = models.CharField(max_length=50)
    DTWind = models.CharField(max_length=60)
    timestamp = models.DateTimeField

class NightTime_Weather(models.Model):
    Low_Temp = models.CharField(max_length=20)
    NTWea = models.CharField(max_length=50)
    NTWind = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True)

class Days6_Weather(models.Model):
    Temp = models.CharField(max_length=50)
    Wea = models.CharField(max_length=60)
    Wind = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True)
