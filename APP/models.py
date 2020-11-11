from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models import Manager as GeoManager

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.TextField()
    geo_location = models.PointField(srid=4326, null=True,blank=True)

    def __str__(self):
        return self.name
