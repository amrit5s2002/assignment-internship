from django.db import models

# Create your models here.

class Sample(models.Model):
    symbol = models.CharField(max_length=20)
    Rank = models.IntegerField()
    Date = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f"{self.symbol}"