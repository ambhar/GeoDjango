
from rest_framework.serializers import ModelSerializer
from providers.models import Provider, Service

class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = [
            'name',
            'email',
            'phone_number',
            'language',
            'currency'
        ]
        
class ProviderDetailSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = [
            'id',
            'name',
            'email',
            'phone_number',
            'language',
            'currency'
        ]
    
class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'provider',
            'name',
            'price',
            'polygon'
        ]

class ServiceDetailSerializer(ModelSerializer):
    provider = ProviderSerializer()
    class Meta:
        model = Service
        fields = [
            'id',
            'provider',
            'name',
            'price',
            'polygon'
        ]
    
    