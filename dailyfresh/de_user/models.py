from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharFieid(max_length=20)
    upwd = models.CharField(max_length=40)
    
    def __str__(self):
        return '%d'%self.id