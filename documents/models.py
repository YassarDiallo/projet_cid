from django.db import models
from accounts.models import *

class Document(models.Model):
    extrait = models.FileField(upload_to='extraits', verbose_name='Extrait')
    certificat = models.FileField(upload_to='certificats', verbose_name='Certificat')
    photos = models.FileField(upload_to='photos/', verbose_name='Photos')
    reçu = models.FileField(upload_to='recus', verbose_name='Reçu')
    author= models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True)
    etat = models.BooleanField(default=False)


    class Meta:
        db_table = "documents"