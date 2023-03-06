from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','user_id', 'product_brand','product_name', 'product_type', 'product_price']
        depth = 1