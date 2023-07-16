from rest_framework import serializers
from gimmeapi.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for products"""

    class Meta:
        model = Product
        fields = ('id', 
                  'category_id', 
                  'seller_id',
                  'name',
                  'price',
                  'description',
                  'stock',
                  'image_url',
                  )
        depth = 2
