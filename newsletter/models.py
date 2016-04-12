from django.db import models
import urllib2, json, httplib2, simplejson, six




# Create your models here.


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __unicode__(self): #python 3 is __str__
        return self.email

class SearchLocation(models.Model):
    city_name = models.CharField(max_length=100, blank=True, null=True)
    location = []

    def __unicode__(self):
        return self.city_name

class GitSearch(models.Model):
    user_name = models.CharField(max_length=100, blank=True, null=True)
    followers = ""
    image = ""

    def __unicode__(self):
        return self.user_name
