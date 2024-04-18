from rest_framework import serializers

from api.models import Machines,Production_log


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Machines
        fields="__all__"


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Production_log
        fields="__all__"

        extra_kwargs = {
            'start_time': {'input_formats': ['%Y-%m-%dT%H:%M:%S']},
            'end_time': {'input_formats': ['%Y-%m-%dT%H:%M:%S']},
        }