from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from .filters import CarFilter,CarFilterNoAut, ComplaintsFilter, MaintenanceFilter
from .forms import CreateCarForm, CreateComplaintsForm, CreateMaintenanceForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Car, Complaints, Drive_axle_model, Engine_model, Failure_node, Maintenance, Recovery_method, Service_company, Steerable_axle_model, Technique_model, Transmission_model, Type_maintenance


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
    
    # def get_queryset(self): # Надо отфильтровать список под клиента, если вошёл под клиентом
    #     queryset = Car.objects.filter(client__user=self.request.user)
    #     self.filterset = CarFilter(self.request.GET, queryset)
    #     return self.filterset.qs

    # def get_context_data(self, **kwargs):
    #      context = super().get_context_data(**kwargs)
    #      context['filterset']=self.filterset
    #      return context

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
    else:
        if type == "engineModel":
            namegroup = 'Модель двигателя'
            item = Engine_model.objects.get(id=id)
        else:
            if type == "transmissionModel":
                namegroup = 'Модель трансмиссии'
                item = Transmission_model.objects.get(id=id)
            else:
                if type == "driveAxleModel":
                    namegroup = 'Модель техники'
                    item = Drive_axle_model.objects.get(id=id)
                else:
                    if type == "steerableAxleModel":
                        namegroup = 'Модель техники'
                        item = Steerable_axle_model.objects.get(id=id)
                    else:
                        if type == "ServiceCompany":
                            namegroup = 'Модель техники'
                            item = Service_company.objects.get(id=id)
    return render(request, 'dictionary.html', {'item': item, 'namegroup' : namegroup})

def maintenancedirectory (request, id, type):

    if type == "typeMaintenance":
        item = Type_maintenance.objects.get(id=id)
    else:
        if type == "serviceCompany":
            item = Service_company.objects.get(id=id)
    return render(request, 'dictionary.html', {'item': item})

def complaintdirectory (request, id, type):

    if type == "failureNode":
        item = Failure_node.objects.get(id=id)
    else:
        if type == "recoveryMethod":
            item = Recovery_method.objects.get(id=id)
        else:
            if type == "serviceCompany":
                item = Service_company.objects.get(id=id)
    return render(request, 'dictionary.html', {'item': item})
                
    
#    form = Directory(request.POST)
#    if form.is_valid():
#        form.save()
#        name = form.cleaned_data.get('name')
#        description = form.cleaned_data.get('description')
#        return redirect('/')

class CarList(ListView): #Общий список машин
    model = Car
    ordering = 'shipping_date'
    template_name = 'cars.html'
    context_object_name = 'cars'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.has_perm('silant.view_car_noclient') == False: # авторизованный пользователь не имеет право просмотра всех записей машин
                queryset = Car.objects.filter(client=self.request.user)
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
    
def dictionaries (request):
    return render(request, 'dictionaries.html')
    

class MaintenanceList(PermissionRequiredMixin, ListView): #Общий список ТО
    model = Maintenance
    ordering = 'date_work_order'
    template_name = 'Maintenance/Maintenances.html'
    permission_required = ('silant.view_maintenance',)
    context_object_name = 'maintenances'
    paginate_by = 10

    def get_queryset(self):
       # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = MaintenanceFilter(self.request.GET, queryset)
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
    
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())          

#РЕКЛАМАЦИИ
class ComplaintsList(LoginRequiredMixin, ListView): #Общий список
    model = Complaints
    ordering = 'date_of_refusal'
    template_name = 'Complaints/Complaints.html'
    permission_required = ('silant.view_complaints',)
    context_object_name = 'complaints'
    paginate_by = 10

    def get_queryset(self):
       # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = ComplaintsFilter(self.request.GET, queryset)
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