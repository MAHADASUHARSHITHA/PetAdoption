from django.db import models

# Create your models here.
class Roles(models.Model):
    role_id = models.IntegerField(blank=False,primary_key=True)
    role_type = models.CharField(max_length=20,blank=False)
    class Meta :
        db_table="roles"
class Users(models.Model):
    user_id    = models.IntegerField(blank=False,primary_key=True)
    username   = models.CharField(max_length=100,blank=False,unique=True)
    email      = models.EmailField()
    password   = models.CharField(max_length=100,blank=False)
    first_name = models.CharField(max_length=100,blank=False)
    last_name  = models.CharField(max_length=100,blank=False)
    is_active  = models.BooleanField(blank=False,default='FALSE')
    role       = models.ForeignKey(Roles,on_delete=models.CASCADE)

    class Meta :
        db_table="users"