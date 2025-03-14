from rest_framework import viewsets
from .models import ViewsData
from .serializers import ViewsDataSerializer

class ViewsDataViewSet(viewsets.ModelViewSet):
    queryset = ViewsData.objects.all()
    serializer_class = ViewsDataSerializer
