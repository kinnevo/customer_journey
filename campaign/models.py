from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone

class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    campaign_name = models.CharField(max_length=80, default="")
    description = models.CharField(max_length=200, default="")
    owner = models.ForeignKey(User)
#        models.CharField(max_length=20, default="admin")  #find the username !!!!!
#    username = models.ForeignKey(User)

    created  = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    campaign_sequence = models.IntegerField( default=0)
    participants = models.IntegerField(default=0)
    visits = models.IntegerField(default=0)

    STATUS_CHOICES = (
        ('A', 'Active'),
        ('P', 'Paused'),
        ('I', 'Inactive'),
    )
#    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='I')
    status = models.CharField(max_length=10,  default='Inactive')

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.campaign_id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Campaign, self).save(*args, **kwargs)

class Newsletter(models.Model):
    newsletter_id = models.AutoField(primary_key=True)
    campaign = models.IntegerField(default=0)
    sequence = models.IntegerField(default=0)
    post1 = models.IntegerField( default=0)
    post2 = models.IntegerField( default=0)
    post3 = models.IntegerField( default=0)
    post4 = models.IntegerField( default=0)
    post5 = models.IntegerField( default=0)
    post6 = models.IntegerField( default=0)
    post7 = models.IntegerField( default=0)
    post8 = models.IntegerField( default=0)

class Newsletter_Sent(models.Model):
    user_id = models.IntegerField(default=0)
    campaign_id = models.IntegerField(default=0)
    sequence = models.IntegerField(default=0)
    post1 = models.IntegerField( default=0)
    post2 = models.IntegerField( default=0)
    post3 = models.IntegerField( default=0)
    post4 = models.IntegerField( default=0)
    post5 = models.IntegerField( default=0)
    post6 = models.IntegerField( default=0)
    post7 = models.IntegerField( default=0)
    post8 = models.IntegerField( default=0)
    post8_visit = models.IntegerField(default=0)
    post8_shared = models.IntegerField(default=0)


class User_Profile(models.Model):
    username = models.ForeignKey(User)
    current_campaign = models.IntegerField(default=0)
    current_sequence = models.IntegerField(default=0)
    priority1 = models.IntegerField( default=0)
    priority2 = models.IntegerField( default=0)
    priority3 = models.IntegerField( default=0)
    priority4 = models.IntegerField( default=0)
    priority5 = models.IntegerField( default=0)
    priority6 = models.IntegerField( default=0)
    priority7 = models.IntegerField( default=0)
    priority8 = models.IntegerField( default=0)

"""
    total_visits = models.IntegerField(default=0)
    total_clicks = models.IntegerField(default=0)
"""
