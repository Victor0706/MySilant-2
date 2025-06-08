from django.urls import path
from .views import MachineListView, MaintenanceListView, ComplaintListView, UserListView, MachineDetailView, MachineUpdateView, MachineCreateView, MachineDeleteView, MaintenanceDetailView, MaintenanceUpdateView, MaintenanceDeleteView, MaintenanceCreateView
from .views import ComplaintDetailView, ComplaintUpdateView, ComplaintDeleteView, ComplaintCreateView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/machines/', MachineListView.as_view(), name='machine_list'),
    path('api/machines/<int:id>', MachineDetailView.as_view(), name='machine_detail'),
    path('api/machines/<int:id>/update', MachineUpdateView.as_view(), name='machine_update'),
    path('api/machines/<int:id>/delete', MachineDeleteView.as_view(), name='machine_delete'),
    path('api/machines/create/', MachineCreateView.as_view(), name='machine_create'),
    path('api/maintenances/', MaintenanceListView.as_view(), name='maintenance_list'),
    path('api/maintenances/<int:id>', MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('api/maintenances/<int:id>/update', MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('api/maintenances/<int:id>/delete', MaintenanceDeleteView.as_view(), name='maintenance_delete'),
    path('api/maintenances/create/', MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('api/complaints/', ComplaintListView.as_view(), name='complaint_list'),
    path('api/complaints/<int:id>', ComplaintDetailView.as_view(), name='complaint_detail'),
    path('api/complaints/<int:id>/update', ComplaintUpdateView.as_view(), name='complaint_update'),
    path('api/complaints/<int:id>/delete', ComplaintDeleteView.as_view(), name='complaint_delete'),
    path('api/complaints/create/', ComplaintCreateView.as_view(), name='complaint_create'),
    path('api/users/', UserListView.as_view(), name='user_list'),
]