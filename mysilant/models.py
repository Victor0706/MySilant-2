from django.db import models
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Service_Company(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name
       

class Model_of_equipment(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Engine_model(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Transmission_model(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Model_of_driving_axle(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Model_of_controlled_bridge(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Machine(models.Model):
    machine_number = models.CharField(max_length=64)
    model_of_equipment = models.ForeignKey(Model_of_equipment, on_delete=models.CASCADE)
    engine_model = models.ForeignKey(Engine_model, on_delete=models.CASCADE)
    engine_number = models.CharField(max_length=64)
    transmission_model = models.ForeignKey(Transmission_model, on_delete=models.CASCADE)
    transmission_number = models.CharField(max_length=64)
    model_of_driving_axle = models.ForeignKey(Model_of_driving_axle, on_delete=models.CASCADE)
    drive_axle_number = models.CharField(max_length=64)
    model_of_controlled_bridge = models.ForeignKey(Model_of_controlled_bridge, on_delete=models.CASCADE)
    controlled_bridge_number = models.CharField(max_length=64)
    supply_contract_number = models.CharField(max_length=64)
    shipment_date = models.DateField()
    consignee = models.CharField(max_length=64)
    delivery_address = models.CharField(max_length=64)
    equipment = models.CharField(max_length=128)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service_company = models.ForeignKey(Service_Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.machine_number
    
    def get_absolute_url(self):
        return reverse('machine_list')


class Type_of_maintenance(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Organization_maintenance(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Maintenance(models.Model):
    type_of_maintenance = models.ForeignKey(Type_of_maintenance, on_delete=models.CASCADE)
    date_of_maintenance = models.DateField()
    development = models.IntegerField(default=0)
    work_order_number = models.CharField(max_length=64)
    work_order_date = models.DateField()
    organization_maintenance = models.ForeignKey(Organization_maintenance, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey(Service_Company, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type_of_maintenance)
    
    def get_absolute_url(self):
        return reverse('maintenance_list')


class Failure_node(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Recovery_method(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Complaint(models.Model):
    date_of_refusal = models.DateField()
    development = models.IntegerField(default=0)
    failure_node = models.ForeignKey(Failure_node, on_delete=models.CASCADE)
    description_of_failure = models.CharField(max_length=64)
    recovery_method = models.ForeignKey(Recovery_method, on_delete=models.CASCADE)
    used_spare_parts = models.CharField(max_length=64)
    date_of_restoration = models.DateField()
    machine_downtime = models.IntegerField(default=0)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey(Service_Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.description_of_failure
    
    def get_absolute_url(self):
        return reverse('complaint_list')


