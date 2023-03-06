from rest_framework import serializers
from .models import Diver

class DiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diver
        fields = ['user_city', 'user_state', 'user_country', 'user_type', 'user_cert_agency', 'user_cert_level', 'user_availibility','user']
        depth = 1