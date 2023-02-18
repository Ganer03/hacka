from django.shortcuts import render
from API.models import Landlord, Leaser, Building, CommercialObject, Position, Personal, Service, \
    HcsType, Hcs
from rest_framework import generics, viewsets, mixins
from API.serializers import LandLordSerializer, LeaserSerializer, BuildingSerializer, CommercialObjectSerializer, \
    PositionSerializer, PersonalSerializer, ServiceSerializer, HcsTypeSerializer, HcsSerializer


class Landlords(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Landlord.objects.all()
    serializer_class = LandLordSerializer


class Leasers(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
              mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Leaser.objects.all()
    serializer_class = LeaserSerializer


class Buildings(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class CommercialObjects(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = CommercialObject.objects.select_related('leaser')
    serializer_class = CommercialObjectSerializer


class Positions(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class Personals(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer


class Services(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
               mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class HcsTypes(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
               mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = HcsType.objects.all()
    serializer_class = HcsTypeSerializer


class Hcss(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
           mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Hcs.objects.prefetch_related("hcs_type")
    serializer_class = HcsSerializer

def free_home(request, pk):
    try:
        user = get_object_or_404(models.Building.objects.prefetch_related('buildings', 'rooms'), user=request.user)
    except Http404:
        return redirect('')
    try:
        user = get_object_or_404(Building.objects.filter(), user = request.user)
        return JsonResponse({'data': [1, 2]})
    except Http404:
        return redirect('')