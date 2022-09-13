from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def post(self, request):
    #     if 'name' in request.data and 'description' in request.data:
    #         new_sensor = Sensor(name=request.data['name'], description=request.data['description']).save()
    #     return Response({'status': f"sensor {request.data['name']} - successfully registered!"})


class SensorUpdateView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # def post(self, request, pk, *args, **kwargs):
    #     if Sensor.objects.all().filter(id=pk).exists():
    #         current_sensor = Sensor.objects.get(id=pk)
    #         temperature = Measurement(temperature=request.data['temperature']).save()
    #         current_sensor.measurements.append(temperature)
    #         return Response({'status': f'Ok'})
    #     else:
    #         return Response({'status': f'сенсор не существует'})


class MeasurementDetailView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
