from django.db import models
from datetime import datetime
from dive_site.models import Dive_Site
from diver.models import User

class DS_Review(models.Model):
    dive_site = models.ForeignKey(Dive_Site, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    review_date = models.DateTimeField(default=datetime.now(), blank=True)
    review_text = models.CharField(max_length=500)
