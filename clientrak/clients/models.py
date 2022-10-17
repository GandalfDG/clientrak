from django.db import models
import datetime

class Agent(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    minimum_rate = models.DecimalField(max_digits=8, decimal_places=2)


class Client(models.Model):
    client_first_name = models.CharField(max_length=256)
    client_last_name = models.CharField(max_length=256)
    agent = models.ForeignKey(Agent, models.CASCADE, null=True)

    def __str__(self):
        return f'{self.client_last_name}, {self.client_first_name}'


class Trip(models.Model):
    trip_name = models.CharField(max_length=1024)
    commission = models.DecimalField(max_digits=8, decimal_places=2)
    time_spent = models.DurationField()
    client = models.ForeignKey(Client, models.CASCADE, null=True)

    def effective_hourly_rate(self):
        worked_hours = self.time_spent.total_seconds() / 3600
        rate = self.client_commission / worked_hours
        return rate