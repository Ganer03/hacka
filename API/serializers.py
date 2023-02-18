from rest_framework import serializers
from API.models import Landlord, Leaser, Building, CommercialObject, Position, Personal, Service, \
    HcsType, Hcs


class LandLordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = [
            'name',
            'surname',
            'patronymic',
            'email',
            'password',
            'get_buildings',
            'get_commercial_objects',
            'incomer',
            'expense'
        ]
        read_only_fields = ['update_time', 'creation_time']


class CommercialObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommercialObject
        fields = [
            'pointer',
            'building',
            'building_address',
            'leaser',
            'leaser_name',
            'rent_price',
            'square',
            'description',
            'document',
            'get_hcs'
        ]
        read_only_fields = ['update_time', 'creation_time']


class LeaserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaser
        fields = [
            'name',
            'surname',
            'patronymic',
            'email',
            'password',
            'get_commercial_objects'
        ]
        read_only_fields = ['update_time', 'creation_time']


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = [
            'name_build',
            'landlord',
            'address',
            'personal',
            'get_personal',
            'services',
            'get_services',
            'income',
            'expenses'
        ]
        read_only_fields = ['update_time', 'creation_time']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'position_name',
            'salary'
        ]
        read_only_fields = ['update_time', 'creation_time']


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = [
            'name',
            'surname',
            'patronymic',
            'email',
            'phone',
            'position',
            'get_salary',
            'get_pos_name'
        ]
        read_only_fields = ['update_time', 'creation_time']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'price',
            'name',
            'description'
        ]
        read_only_fields = ['update_time', 'creation_time']


class HcsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcsType
        fields = ['name']
        read_only_fields = ['update_time', 'creation_time']


class HcsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hcs
        fields = [
            'hcs_type',
            'value'
        ]
        read_only_fields = ['update_time', 'creation_time']
