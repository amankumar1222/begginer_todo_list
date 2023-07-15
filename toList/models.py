from django.db import models

# Create your models here.
class todo(models.Model):
    
    task = models.CharField(max_length=300)

    

