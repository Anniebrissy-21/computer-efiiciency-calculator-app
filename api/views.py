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
        print(production_logs)
    return JsonResponse(oee_data, safe=False)

def calculate_oee(production_logs):
    ideal_cycle_time = 5  # Ideal cycle time is 5 minutes
    total_products = production_logs.count()  # Use count() to get the number of logs
    
    # Ensure total_products is not zero
    if total_products == 0:
        return 0  # Return zero if no production logs
    
    good_products = production_logs.filter(duration=ideal_cycle_time).count()
    unplanned_downtime = 0  # You may adjust this based on your actual data or logic
    availability = (24 * 3 - unplanned_downtime) / (24 * 3) * 100  # Assuming 3 shifts of 8 hours each
    performance = (good_products * ideal_cycle_time) / (total_products * ideal_cycle_time) * 100
    quality = (good_products / total_products) * 100
    
    oee = availability * performance * quality / 10000  # Convert percentages to a scale of 0 to 100
    print(total_products)
    print(good_products)
    print(availability)
    print(performance)
    return oee