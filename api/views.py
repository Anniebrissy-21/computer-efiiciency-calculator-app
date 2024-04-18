from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import views,viewsets
from rest_framework.response import Response
from api.models import Machines,Production_log
from api.serializer import MachineSerializer,ProductionSerializer


class MachineView(viewsets.ModelViewSet):
    serializer_class=MachineSerializer
    queryset=Machines.objects.all()

class ProductionLogView(viewsets.ModelViewSet):
    serializer_class=ProductionSerializer
    queryset=Production_log.objects.all()

@api_view(['GET'])
def oee_data(request):
    machines = Machines.objects.all()
    oee_data = []
    for machine in machines:
        production_logs = Production_log.objects.filter(machine=machine)
        oee = calculate_oee(production_logs)
        oee_data.append({'machine_name': machine.machine_name, 'oee': oee})
    return JsonResponse(oee_data, safe=False)

def calculate_oee(production_logs):
    ideal_cycle_time = 5  # Ideal cycle time is 5 minutes
    total_products = len(production_logs)
    
    # Ensure total_products is not zero
    if total_products == 0:
        return 0  # Return zero if no production logs
    
    good_products = sum(1 for log in production_logs if log.duration == ideal_cycle_time)
    unplanned_downtime=0
    availability = 100 - (unplanned_downtime / (24 * 3)) * 100  # Assuming 3 shifts of 8 hours each
    performance = (ideal_cycle_time * total_products) / (total_products * ideal_cycle_time) * 100
    quality = (good_products / total_products) * 100
    return availability * performance * quality


