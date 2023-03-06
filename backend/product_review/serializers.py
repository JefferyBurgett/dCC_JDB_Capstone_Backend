from rest_framework import serializers
from .models import Product_Review

class ProductReviewSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product_Review
        fields = ['user', 'product_id', 'user_id', 'pd_review_date', 'pd_review_text']
        depth = 1