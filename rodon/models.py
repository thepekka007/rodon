from django.db import models

# Create your models here.
class Contactdata(models.Model):
  
    name = models.CharField( max_length=150,null=True, blank=True)
    email = models.CharField( max_length=150,null=True, blank=True)
    subject = models.CharField( max_length=150,null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    phone = models.CharField( max_length=150,null=True, blank=True)
    # name = models.CharField( max_length=150,null=True, blank=True)
  