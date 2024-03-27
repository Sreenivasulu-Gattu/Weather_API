from django.db import models

# Create your models here.
from datetime import datetime,timedelta
import pytz

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    humidity = models.DecimalField(max_digits=5, decimal_places=1)
    weather=models.CharField(max_length=10,default=0)
    speed=models.CharField(max_length=10,default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Weather in {self.city} at {self.timestamp}"
    
