from django.db import models

# Create your models here.

SUBSCRIPTION_PLANS = [
    ('W', 'Weekly'),
    ('M', 'Monthly'),
    ('Y', 'Yearly')
]
class Subscriber(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    plan = models.CharField(max_length=2, choices=SUBSCRIPTION_PLANS, default='W')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"