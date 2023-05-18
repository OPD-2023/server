from rest_framework import serializers

from server.models import Partner, Direction, History, Product, Service, SubService, Contact


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


class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = ['id', 'description']


class ServiceSerializer(serializers.ModelSerializer):
    sub_services = SubServiceSerializer(many=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'sub_services']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'description', 'status', 'image_path']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['address', 'phones', 'emails']