from django.conf.urls import url
from .views import (
    ProviderCreateAPIView, 
    ProviderListAPIView, 
    ProviderDetailAPIView, 
    ProviderUpdateAPIView, 
    ProviderDeleteAPIView, 

    ServiceListAPIView,
    ServiceCreateAPIView,
    ServiceDetailAPIView,
    ServiceDeleteAPIView,
    ServiceUpdateAPIView,
    SearchedServiceListAPIView
    )

urlpatterns = [
    url(r'^provider/create/$', ProviderCreateAPIView.as_view(), name='create'),
    url(r'^provider/list/$', ProviderListAPIView.as_view(), name='list'),
    url(r'^provider/(?P<id>\d+)/detail/$', ProviderDetailAPIView.as_view(), name='detail'),
    url(r'^provider/(?P<id>\d+)/edit/$', ProviderUpdateAPIView.as_view(), name='update'),
    url(r'^provider/(?P<id>\d+)/delete/$', ProviderDeleteAPIView.as_view(), name='delete'),

    url(r'^service/create/$', ServiceCreateAPIView.as_view(), name='create'),
    url(r'^service/list/$', ServiceListAPIView.as_view(), name='list'),
    url(r'^service/(?P<id>\d+)/detail/$', ServiceDetailAPIView.as_view(), name='detail'),
    url(r'^service/(?P<id>\d+)/edit/$', ServiceUpdateAPIView.as_view(), name='update'),
    url(r'^service/(?P<id>\d+)/delete/$', ServiceDeleteAPIView.as_view(), name='delete'),

    url(r'^service/(?P<coordinates>[\w|\W|%20]+)/list/$', SearchedServiceListAPIView.as_view(), name='searchedlist'),
]
