from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .filters import CarFilter,CarFilterNoAut, ComplaintsFilter, MaintenanceFilter
from .forms import CreateCarForm, CreateComplaintsForm, CreateMaintenanceForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Car, Complaints, Drive_axle_model, Engine_model, Failure_node, Maintenance, Organization_maintenance, Recovery_method, Service_company, Steerable_axle_model, Technique_model, Transmission_model, Type_maintenance


class CarCreate(PermissionRequiredMixin, CreateView):
    model = Car
    form_class = CreateCarForm
    template_name = 'CreateCar.html'
    permission_required = ('silant.add_car',)
    success_url = '/cars/'

    def form_valid(self, form): #редирект на список
         self.object = form.save(commit=False)
         self.object.user = self.request.user
         self.object.save()
         return redirect(self.get_success_url())
    
class CarEdit(PermissionRequiredMixin, UpdateView):
    form_class = CreateCarForm
    model = Car
    template_name = 'CreateCar.html'
    permission_required = ('silant.change_car', )
    success_url = '/cars/'

    def form_valid(self, form): #редирект на список
         self.object = form.save(commit=False)
         self.object.user = self.request.user
         self.object.save()
         return redirect(self.get_success_url())

def cardirectory (request, id, type): #Функция по форме отображения каждого справочника Модель 

    if type == "techniqueModel":
        namegroup = 'Модель техники'
        item = Technique_model.objects.get(id=id)
    elif type == "engineModel":
        namegroup = 'Модель двигателя'
        item = Engine_model.objects.get(id=id)
    elif type == "transmissionModel":
        namegroup = 'Модель трансмиссии'
        item = Transmission_model.objects.get(id=id)
    elif type == "driveAxleModel":
        namegroup = 'Модель ведущего моста'
        item = Drive_axle_model.objects.get(id=id)
    elif type == "steerableAxleModel":
        namegroup = 'Модель управляемого моста'
        item = Steerable_axle_model.objects.get(id=id)
    elif type == "ServiceCompany":
        namegroup = 'Сервисная организация'
        item = Service_company.objects.get(id=id)
    return render(request, 'dictionary.html', {'item': item, 'namegroup' : namegroup, 'type' : type})

def maintenancedirectory (request, id, type):

    if type == "typeMaintenance":
        namegroup = 'Вид ТО'    
        item = Type_maintenance.objects.get(id=id)
    elif type == "serviceCompany":
        namegroup = 'Сервисная организация'
        item = Service_company.objects.get(id=id)
    elif type == "organizationMaintenance":
        namegroup = 'Организация, проводившая ТО'
        item = Organization_maintenance.objects.get(id=id) 
    return render(request, 'dictionary.html', {'item': item, 'namegroup' : namegroup, 'type' : type})

def complaintdirectory (request, id, type):

    if type == "failureNode":
        namegroup = 'Узел отказа'
        item = Failure_node.objects.get(id=id)
    elif type == "recoveryMethod":
        namegroup = 'Способ восстановления'
        item = Recovery_method.objects.get(id=id)
    elif type == "serviceCompany":
        namegroup = 'Сервисная организация'
        item = Service_company.objects.get(id=id)
    return render(request, 'dictionary.html', {'item': item, 'namegroup' : namegroup, 'type' : type})
                

class CarList(ListView): #Общий список машин
    model = Car
    ordering = 'shipping_date'
    template_name = 'cars.html'
    context_object_name = 'cars'
    paginate_by = 5


    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.has_perm('silant.view_car_noclient') == False: # авторизованный пользователь не имеет право просмотра всех записей машин
                queryset = Car.objects.filter(client__user=self.request.user)
            else:
                if self.request.user.has_perm('silant.view_car_noservice') == False:
                    queryset = Car.objects.filter(service_company__user=self.request.user)
            self.filterset = CarFilter(self.request.GET, queryset)
        else:
            if not bool(self.request.GET):
                queryset = Car.objects.none()
            self.filterset = CarFilterNoAut(self.request.GET, queryset)          
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    

class CarDetail(DetailView):
    model = Car
    template_name = 'CarDetail.html'
    context_object_name = 'car'


# ТЕХНИЧЕСКОЕ ОБСЛУЖИАНИЕ
class MaintenanceList(PermissionRequiredMixin, ListView): #Общий список ТО
    model = Maintenance
    ordering = 'date_work_order'
    template_name = 'Maintenance/Maintenances.html'
    permission_required = ('silant.view_maintenance',)
    context_object_name = 'maintenances'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.has_perm('silant.view_maintenance_noclient') == False: # авторизованный пользователь не имеет право просмотра всех записей машин
                queryset = Maintenance.objects.filter(car__client__user=self.request.user)
            else:
                if self.request.user.has_perm('silant.view_maintenance_noservice') == False:
                    queryset = Maintenance.objects.filter(service_company__user=self.request.user)
            self.filterset = MaintenanceFilter(self.request.GET, queryset)
        else:
            if not bool(self.request.GET):
                queryset = Maintenance.objects.none()
        return self.filterset.qs
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class MaintenanceCreate(PermissionRequiredMixin, CreateView):
    model = Maintenance
    form_class = CreateMaintenanceForm
    template_name = 'Maintenance/CreateMaintenance.html'
    permission_required = ('silant.add_maintenance',)
    success_url = '/cars/maintenances/'

    def form_valid(self, form): #редирект на список
         self.object = form.save(commit=False)
         self.object.user = self.request.user
         self.object.save()
         return redirect(self.get_success_url())
    
class MaintenanceEdit(PermissionRequiredMixin, UpdateView):
    form_class = CreateMaintenanceForm
    model = Maintenance
    template_name = 'Maintenance/CreateMaintenance.html'
    permission_required = ('silant.change_maintenance', )
    success_url = '/cars/maintenances/'

    def form_valid(self, form): #редирект на список
         self.object = form.save(commit=False)
         self.object.user = self.request.user
         self.object.save()
         return redirect(self.get_success_url())

#РЕКЛАМАЦИИ
class ComplaintsList(LoginRequiredMixin, ListView): #Общий список
    model = Complaints
    ordering = 'date_of_refusal'
    template_name = 'Complaints/Complaints.html'
    permission_required = ('silant.view_complaints',)
    context_object_name = 'complaints'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_authenticated:
            if self.request.user.has_perm('silant.view_complaints_noclient') == False: # авторизованный пользователь не имеет право просмотра всех записей машин
                queryset = Complaints.objects.filter(car__client__user=self.request.user)
            else:
                if self.request.user.has_perm('silant.view_complaints_noservice') == False:
                    queryset = Complaints.objects.filter(service_company__user=self.request.user)
            self.filterset = ComplaintsFilter(self.request.GET, queryset)
        else:
            if not bool(self.request.GET):
                queryset = Complaints.objects.none()
        return self.filterset.qs
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class ComplaintsCreate(PermissionRequiredMixin, CreateView):
    model = Complaints
    form_class = CreateComplaintsForm
    template_name = 'Complaints/CreateComplaints.html'
    permission_required = ('silant.add_complaints',)
    success_url = '/cars/complaints/'

    
    def form_valid(self, form): #редирект на список
         self.object = form.save(commit=False)
         self.object.user = self.request.user
         self.object.save()
         return redirect(self.get_success_url())
    

class ComplaintsEdit(PermissionRequiredMixin, UpdateView):
    form_class = CreateComplaintsForm
    model = Complaints
    template_name = 'Complaints/CreateComplaints.html'
    permission_required = ('silant.change_complaints', )
    success_url = '/cars/complaints/'

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


def savedictionary(request): 
    # form = NewsForm(request.POST)
    print(request.POST)
    id = request.POST['id']
    type = request.POST['type']
    name = request.POST['name']
    description = request.POST['description']
    if type == "techniqueModel":
        model = Technique_model.objects.get(id=id)
        model.name = name
        model.description = description
        Technique_model.save(model)
    elif type == "engineModel":
        model = Engine_model.objects.get(id=id)
        model.name = name
        model.description = description
        Engine_model.save(model)
    elif type == "transmissionModel":
        model = Transmission_model.objects.get(id=id)
        model.name = name
        model.description = description
        Transmission_model.save(model)
    elif type == "driveAxleModel":
        model = Drive_axle_model.objects.get(id=id)
        model.name = name
        model.description = description
        Drive_axle_model.save(model)
    elif type == "steerableAxleModel":
        model = Steerable_axle_model.objects.get(id=id)
        model.name = name
        model.description = description
        Steerable_axle_model.save(model)
    elif type == "ServiceCompany":
        model = Service_company.objects.get(id=id)
        model.name = name
        model.description = description
        Service_company.save(model)                    
    elif type == "typeMaintenance":
        model = Type_maintenance.objects.get(id=id)
        model.name = name
        model.description = description
        Type_maintenance.save(model)
    elif type == "organizationMaintenance":
        model = Organization_maintenance.objects.get(id=id)
        model.name = name
        model.description = description
        Organization_maintenance.save(model)
    elif type == "failureNode":
        model = Failure_node.objects.get(id=id)
        model.name = name
        model.description = description
        Failure_node.save(model)
    elif type == "recoveryMethod":
        model = Recovery_method.objects.get(id=id)
        model.name = name
        model.description = description
        Recovery_method.save(model)      

    return redirect('/')
