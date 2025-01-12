from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status



from serializers import *



# -------------------------- volume ------------------------------------------------------
class VolumeRetrieveView(generics.RetrieveAPIView):
    serializer_class = VolumeSerializer
    queryset = Volume.objects.all()

class VolumeUpdateView(generics.UpdateAPIView):
    serializer_class = VolumeSerializer
    queryset = Volume.objects.all()


class VolumeCreateView(generics.CreateAPIView):
    serializer_class = CreateVolumeSerializer
    queryset = Volume.objects.all()


class VolumeListView(generics.ListAPIView):
    serializer_class = VolumeSerializer
    queryset = Volume.objects.all()


class VolumeDeleteView(generics.DestroyAPIView):
    serializer_class = VolumeSerializer
    queryset = Volume.objects.all()


