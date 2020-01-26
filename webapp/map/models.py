from django.db import models

class Accident(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    start_lat = models.DecimalField(decimal_places=5, max_digits=8)
    end_lat = models.DecimalField(decimal_places=5, max_digits=8)

    start_long = models.DecimalField(decimal_places=5, max_digits=8)
    end_long = models.DecimalField(decimal_places=5, max_digits=8)

    severity = models.IntegerField()


class QueryItem(models.Model):
    icon = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    query_parameter = models.CharField(max_length=64)


    def __str__(self):
        return "[%d] %s" % (self.id, self.name)