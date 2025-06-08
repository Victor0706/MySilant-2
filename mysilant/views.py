from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Machine, Maintenance, Complaint, Model_of_equipment
from django.contrib.auth.models import User
from .serializers import MachineSerializer, MaintenanceSerializer, ComplaintSerializer, UserSerializer
from .forms import MachineForm, MaintenanceForm, ComplaintForm
from .filters import MachineFilter, MaintenanceFilter, ComplaintFilter, HomeFilter



class HomePageView(ListView):
    model = Machine
    template_name = 'home.html'
    context_object_name = 'machines'

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = HomeFilter(self.request.GET, queryset)
       return self.filterset.qs
       
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context
    

class MachineListView(PermissionRequiredMixin, ListView):
    permission_required = 'mysilant.view_machine'
    form_class = MachineForm
    model = Machine
    ordering = 'shipment_date'
    template_name = 'machines.html'
    context_object_name = 'machines'

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = MachineFilter(self.request.GET, queryset)
       return self.filterset.qs
       
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context
    



class MachineDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'mysilant.view_machine'
    model = Machine
    template_name = 'machine.html'
    context_object_name = 'machine'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()


class MachineCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'mysilant.add_machine'
    form_class = MachineForm
    model = Machine
    template_name = 'machine_edit.html'


class MachineUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'mysilant.change_machine'
    form_class = MachineForm
    template_name = 'machine_edit.html'
    model = Machine
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()
    

class MachineDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'mysilant.delete_machine'
    model = Machine
    template_name = 'machine_delete.html'
    success_url = reverse_lazy('machine_list')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()

    
class MaintenanceListView(PermissionRequiredMixin, ListView):
    permission_required = 'mysilant.view_maintenance'
    model = Maintenance
    ordering = 'date_of_maintenance'
    form_class = MaintenanceForm
    template_name = 'maintenances.html'
    context_object_name = 'maintenances'

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = MaintenanceFilter(self.request.GET, queryset)
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context

    
class MaintenanceDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'mysilant.view_maintenance'
    model = Maintenance
    template_name = 'maintenance.html'
    context_object_name = 'maintenance'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()
    

class MaintenanceCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'mysilant.add_maintenance'
    form_class = MaintenanceForm
    model = Maintenance
    template_name = 'maintenance_edit.html'


class MaintenanceUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'mysilant.change_maintenance'
    form_class = MaintenanceForm
    template_name = 'maintenance_edit.html'
    model = Maintenance
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()


class MaintenanceDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'mysilant.delete_maintenance'
    model = Maintenance
    template_name = 'maintenance_delete.html'
    success_url = reverse_lazy('maintenance_list')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()


class ComplaintListView(PermissionRequiredMixin, ListView):
    permission_required = 'mysilant.view_complaint'
    form_class = ComplaintForm
    model = Complaint
    ordering = 'date_of_refusal'
    template_name = 'complaints.html'
    context_object_name = 'complaints'

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = ComplaintFilter(self.request.GET, queryset)
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context

    
class ComplaintDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'mysilant.view_complaint'
    model = Complaint
    template_name = 'complaint.html'
    context_object_name = 'complaint'
    pk_url_kwarg = 'id'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()


class ComplaintCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'mysilant.add_complaint'
    form_class = ComplaintForm
    model = Complaint
    template_name = 'complaint_edit.html'


class ComplaintUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'mysilant.change_complaint'
    form_class = ComplaintForm
    template_name = 'complaint_edit.html'
    model = Complaint
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()


class ComplaintDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'mysilant.delete_complaint'
    model = Complaint
    template_name = 'complaint_delete.html'
    success_url = reverse_lazy('complaint_list')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()
    

class UserListView(ListView):
    def get(self, request):
        user = User.objects.get(id=self.request.user.id)
        return Response(user)
    

     

     
     
    

    
    

    
    
        
    





