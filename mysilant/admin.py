from django.contrib import admin
from .models import Client, Service_Company, Model_of_equipment, Engine_model, Transmission_model, Model_of_driving_axle, Model_of_controlled_bridge, Machine, Type_of_maintenance, Maintenance, Failure_node, Recovery_method, Complaint, Organization_maintenance


admin.site.register(Client)
admin.site.register(Service_Company)
admin.site.register(Model_of_equipment)
admin.site.register(Engine_model)
admin.site.register(Transmission_model)
admin.site.register(Model_of_driving_axle)
admin.site.register(Model_of_controlled_bridge)
admin.site.register(Machine)
admin.site.register(Type_of_maintenance)
admin.site.register(Maintenance)
admin.site.register(Failure_node)
admin.site.register(Recovery_method)
admin.site.register(Complaint)
admin.site.register(Organization_maintenance)

