from django import forms
from django.core.exceptions import ValidationError
from .models import Machine, Maintenance, Complaint


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machine_number', 'model_of_equipment', 'engine_model', 'engine_number', 'transmission_model', 'transmission_number', 'model_of_driving_axle', 'drive_axle_number',
                  'model_of_controlled_bridge',  'controlled_bridge_number', 'supply_contract_number', 'shipment_date', 'consignee', 'delivery_address',
                  'equipment', 'client', 'service_company']
        

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['type_of_maintenance', 'date_of_maintenance', 'development', 'work_order_number', 'work_order_date', 'organization_maintenance', 
                  'machine', 'service_company',  ]
        

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['date_of_refusal', 'development', 'failure_node', 'description_of_failure', 'recovery_method', 'used_spare_parts', 'date_of_restoration',
                  'machine_downtime', 'machine', 'service_company']
        

       
                
               
        

        
           

        
    

        

    


    