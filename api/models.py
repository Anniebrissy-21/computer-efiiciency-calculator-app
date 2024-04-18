from django.db import models

# Create your models here.

class Machines(models.Model):
    machine_name = models.CharField(max_length=100)
    machine_serial_no = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.machine_name

class Production_log(models.Model):
    cycle_no = models.CharField(max_length=10)
    unique_id = models.CharField(max_length=100, unique=True)
    material_name = models.CharField(max_length=100)
    machine = models.ForeignKey(Machines, on_delete=models.CASCADE,related_name="machine")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.FloatField()

    def __str__(self):
        return self.material_name
