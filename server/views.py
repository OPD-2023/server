from rest_framework import generics

from server.models import Partner, Direction, Service, Product, History, SubService
from server.serializers import PartnerSerializer, DirectionSerializer, HistorySerializer, ServiceSerializer, \
    ProductSerializer, SubServiceSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PartnerList(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class DirectionList(generics.ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class DirectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SubServiceList(generics.ListCreateAPIView):
    queryset = SubService.objects.all()
    serializer_class = SubServiceSerializer


class SubServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubService.objects.all()
    serializer_class = SubServiceSerializer


class HistoryList(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class HistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
