from rest_framework import serializers
from .models import Machine, Maintenance, Complaint
from django.contrib.auth.models import User


class MachineSerializer(serializers.ModelSerializer):
    model_of_equipment = serializers.StringRelatedField()
    engine_model = serializers.StringRelatedField()
    transmission_model = serializers.StringRelatedField()
    model_of_driving_axle = serializers.StringRelatedField()
    model_of_controlled_bridge = serializers.StringRelatedField()
    client = serializers.StringRelatedField()
    service_company = serializers.StringRelatedField()
    class Meta:
        model = Machine
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    type_of_maintenance = serializers.StringRelatedField()
    organization_maintenance = serializers.StringRelatedField()
    machine = serializers.StringRelatedField()
    service_company = serializers.StringRelatedField()
    class Meta:
        model = Maintenance
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    failure_node = serializers.StringRelatedField()
    recovery_method = serializers.StringRelatedField()
    machine = serializers.StringRelatedField()
    service_company = serializers.StringRelatedField()
    class Meta:
        model = Complaint
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

