from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    users_id = models.ForeignKey(User, models.SET_NULL, blank=True, null=True,)


class Meta:
    ordering = ['-created']


def __unicode__(self):
    return u'%s' % self.title




