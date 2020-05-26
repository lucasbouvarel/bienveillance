# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

# Create your models here.
class Person(models.Model):
    user=models.OneToOneField(User, on_delete=models.SET_NULL,null=True, blank=True)
    vote=models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name="Colloc"
        ordering= ['user']

    def __str__(self):
        return self.user.first_name + " "+ self.user.last_name

class Transaction(models.Model):
    collocDonneur=models.ForeignKey(Person,related_name="collocDonneur",on_delete=models.SET_NULL,null=True, blank=True)
    collocReceveur=models.ForeignKey(Person,related_name="collocReceveur",on_delete=models.SET_NULL,null=True, blank=True)
    point=models.IntegerField(null=False)
    raison=models.TextField(null=True,blank=True)



    class Meta:
        verbose_name="Transaction"
    
