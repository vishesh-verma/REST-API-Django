from rest_framework import serializers
from .models import stock

class stockSerializer(serializers.ModelSerializer):

    class Meta:
        model= stock
        #field= ('ticker','op')
        fields= '__all__'
