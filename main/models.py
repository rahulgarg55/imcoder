from django.db import models

# Create your models here.
class Contact(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField()
    contact = models.CharField(max_length=70)
    desc = models.CharField(max_length=500)
    sub = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class u_log(models.Model):
    p_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=500)

class u_sign(models.Model):
    p_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    pwd1 = models.CharField(max_length=500)
    pwd2 = models.CharField(max_length=500)

