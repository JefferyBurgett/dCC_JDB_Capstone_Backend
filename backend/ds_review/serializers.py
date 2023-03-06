from rest_framework import serializers
from .models import DS_Review

class DS_ReviewSerializer(serializers.ModelSerializer):
    dive_site_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = DS_Review
        fields = ['user','dive_site_id', 'review_date', 'review_text']
        depth = 1