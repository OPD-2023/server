from rest_framework import serializers

from server.models import Partner, Direction, Project, History
from server.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'created_at', 'updated_at']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name']


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ['id', 'description']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'description']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'description']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'description', 'status', 'image_path']
