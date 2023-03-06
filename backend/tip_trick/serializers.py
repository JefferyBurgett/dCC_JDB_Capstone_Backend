from rest_framework import serializers
from .models import Tip_Trick

class Tip_TrickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip_Trick
        fields = ['user','user_id','tt_text']
        depth = 1