from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DroneData
from .serializers import DroneDateSerializer, UploadDroneDataSerializer

# Create your views here.

def main(request):
    return HttpResponse("firddd")

class DroneDataView(generics.ListCreateAPIView):
    queryset=DroneData.objects.all()
    serializer_class=DroneDateSerializer

class UploadDroneDataView(APIView):
    serializer_class=UploadDroneDataSerializer
    
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        print(request.data)
        print('efefe')
        if serializer.is_valid():
            print('nameeeeeeeeeeeee',serializer.data.get('name'))
            dronedata=DroneData(name=serializer.data.get('name'),total_flight_time=serializer.data.get('total_flight_time'))
            dronedata.save()
        return Response({}, status=status.HTTP_200_OK)