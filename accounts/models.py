from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    telephone=models.CharField(max_length=50)
    email=models.EmailField()
    username=models.CharField(max_length=50,unique=True)
    
    class Meta:
        db_table="accounts"
        
    