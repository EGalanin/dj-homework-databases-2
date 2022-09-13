from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorUpdateView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementDetailView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
