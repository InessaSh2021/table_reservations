from django.db import models
from django.utils import timezone


class Table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    seats = models.PositiveIntegerField()
    location = models.TextField()

    def __str__(self):
        return self.name


class Reservations(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField(default=timezone.now)
    duration_minutes = models.IntegerField()

    def __str__(self):
        return self.customer_name