import json
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )


from providers.models import Provider, Service

from .serializers import (
    ProviderSerializer, 
    ProviderDetailSerializer, 
    ServiceSerializer,
    ServiceDetailSerializer
    )
    
# API Views For Provider
class ProviderCreateAPIView(CreateAPIView):
    serializer_class = ProviderSerializer
    #permission_classes = [IsAdminUser]

class ProviderListAPIView(ListAPIView):
    serializer_class = ProviderDetailSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Provider.objects.all() 
        return queryset_list

class ProviderDetailAPIView(RetrieveAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class ProviderUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        

class ProviderDeleteAPIView(DestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]



# API Views For Service

class ServiceListAPIView(ListAPIView):
    serializer_class = ServiceDetailSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Service.objects.all() 
        return queryset_list

class ServiceCreateAPIView(CreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

class ServiceDetailAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ServiceUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
class ServiceDeleteAPIView(DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]

class SearchedServiceListAPIView(ListAPIView): # searching coordinates sent bu user in polygon field
    serializer_class = ServiceDetailSerializer
    def get_queryset(self, *args, **kwargs):
        coordinates = self.kwargs['coordinates'] # from api URL
        coordinates = coordinates.encode('ascii','ignore') # unicode to string
        coordinates = tuple([float(x) for x in coordinates.split(',')]) # convert to float and save as tuple as our polygon points are in form of tuple
        queryset_list = Service.objects.all() 
        
        searched_query = []
        for query in queryset_list: # provide linearstring from polygon
            for coords in query.polygon[0]: # provide points in form of tuple from polygon
                
                if coordinates == coords:
                    searched_query.append(query)
            
        return searched_query
