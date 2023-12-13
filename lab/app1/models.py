from django.db import models
from django.db.models.signals import post_save,post_delete
# Create your models here.
# firstname lastname phoneno email
class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phoneno = models.CharField(max_length=12,help_text='mobile')
    email = models.EmailField()

    def __str__(self):
        return f'''{self.firstname}'''
# name author publisher
class Book(models.Model):
    name = models.CharField(max_length=70)
    author = models.CharField(max_length=70)
    publisher = models.CharField(max_length=70)
    def __str__(self):
        return f'''{self.name}'''

class Issuebook(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    idate = models.DateField(auto_now=True) #give current date not requird on front-end to disply if give it take data from frnt-e
    rdate = models.DateField(blank=True,null=True)

