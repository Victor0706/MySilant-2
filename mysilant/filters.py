from django_filters import FilterSet, ModelChoiceFilter
from .models import Machine, Maintenance, Complaint, Model_of_equipment, Engine_model, Transmission_model, Model_of_driving_axle, Model_of_controlled_bridge, Type_of_maintenance, Service_Company, Failure_node, Recovery_method


class HomeFilter(FilterSet):
    class Meta:
       model = Machine
       fields = {
           'machine_number': ['exact'],
       }

class MachineFilter(FilterSet):
   model_of_equipment = ModelChoiceFilter (
       queryset = Model_of_equipment.objects.all(),
       label = 'Модель техники',
       empty_label = 'любая'
   )

   engine_model = ModelChoiceFilter (
       queryset = Engine_model.objects.all(),
       label = 'Модель двигателя',
       empty_label = 'любая'
   )

   transmission_model = ModelChoiceFilter (
       queryset = Transmission_model.objects.all(),
       label = 'Модель трансмиссии',
       empty_label = 'любая'
   )

   model_of_driving_axle = ModelChoiceFilter (
       queryset = Model_of_driving_axle.objects.all(),
       label = 'Модель ведущего моста',
       empty_label = 'любая'
   )

   model_of_controlled_bridge = ModelChoiceFilter (
       queryset = Model_of_controlled_bridge.objects.all(),
       label = 'Модель управляемого моста',
       empty_label = 'любая'
   )

   class Meta:
       model = Machine
       fields = {
           'model_of_equipment': ['exact'],
           'engine_model': ['exact'],
           'transmission_model': ['exact'],
           'model_of_driving_axle' : ['exact'],
           'model_of_controlled_bridge' : ['exact'],
       }


class MaintenanceFilter(FilterSet):
   type_of_maintenance = ModelChoiceFilter (
       queryset = Type_of_maintenance.objects.all(),
       label = 'Вид ТО',
       empty_label = 'любой'
   )

   machine = ModelChoiceFilter (
       queryset = Machine.objects.all(),
       label = 'Зав. № машины',
       empty_label = 'любой'
   )

   service_company = ModelChoiceFilter (
       queryset = Service_Company.objects.all(),
       label = 'Сервисная компания',
       empty_label = 'любая'
   )

   class Meta:
       model = Maintenance
       fields = {
           'type_of_maintenance': ['exact'],
           'machine': ['exact'],
           'service_company': ['exact'],
       }


class ComplaintFilter(FilterSet):
   failure_node = ModelChoiceFilter (
       queryset = Failure_node.objects.all(),
       label = 'Узел отказа',
       empty_label = 'любой'
   )

   recovery_method = ModelChoiceFilter (
       queryset = Recovery_method.objects.all(),
       label = 'Способ восстановления',
       empty_label = 'любой'
   )

   service_company = ModelChoiceFilter (
       queryset = Service_Company.objects.all(),
       label = 'Сервисная компания',
       empty_label = 'любая'
   )

   class Meta:
       model = Complaint
       fields = {
           'failure_node': ['exact'],
           'recovery_method': ['exact'],
           'service_company': ['exact'],
       }