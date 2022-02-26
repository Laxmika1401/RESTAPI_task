from django.db import models

# Create your models here.
class tva_table(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=500)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip = models.IntegerField()
    email = models.CharField(max_length=200)
    web = models.CharField(max_length=500)
    age = models.IntegerField()
    
    