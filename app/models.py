from django.db import models

class Forecast(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()

    class Meta:
        unique_together = ('city', 'date')

    def __str__(self):
        return f"Прогноз для{self.city} - {self.date}"
        
