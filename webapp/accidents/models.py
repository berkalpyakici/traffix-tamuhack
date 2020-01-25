from django.db import models

class Accident(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    start_lat = models.DecimalField()
    end_lat = models.DecimalField()

    start_long = models.DecimalField()
    end_long = models.DecimalField()

    severity = models.IntegerField()