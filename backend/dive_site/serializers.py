from rest_framework import serializers
from .models import Dive_Site

class DiveSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dive_Site
        fields = ['id','user_id', 'site_name', 'site_city', 'site_state', 'site_country', 'site_lat', 'site_lng']
        depth = 1