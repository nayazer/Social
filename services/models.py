from django.db import models
from datetime import datetime

class Service(models.Model):
  title = models.CharField(max_length=100)
  teaser = models.CharField(blank=True, null=True, max_length=200)
  description = models.TextField(blank=True)
  photo_main = models.ImageField(upload_to='photos')
  is_published = models.BooleanField(default=True)
  date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title
