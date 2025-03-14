from django.db import models

class ViewsData(models.Model):
    url = models.CharField(max_length=100, primary_key=True)  
    title = models.CharField(max_length=1000, blank=True, null=True)
    datetime = models.DateTimeField()  
    views = models.IntegerField()