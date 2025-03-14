from rest_framework import serializers
from .models import ViewsData

class ViewsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewsData
        fields = '__all__' 
