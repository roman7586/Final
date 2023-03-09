from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from .filters import CarFilter,CarFilterNoAut
from .forms import CreateCarForm, CreateComplaintsForm, CreateMaintenanceForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Car, Complaints, Drive_axle_model, Engine_model, Failure_node, Maintenance, Recovery_method, Service_company, Steerable_axle_model, Technique_model, Transmission_model, Type_maintenance


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CreateCarForm
    template_name = 'CreateCar.html'
    permission_required = ('silant.create_car',)
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

class CarEdit(LoginRequiredMixin, UpdateView):
    form_class = CreateCarForm
    model = Car
    template_name = 'CreateCar.html'
    permission_required = ('silant.edit_car', )
    success_url = '/cars/'

    def form_valid(self, form): #редирект на список
         self.object = form.save(commit=False)
         self.object.user = self.request.user
         self.object.save()
         return redirect(self.get_success_url())

def cardirectory (request, id, type): #Функция по форме отображения каждого справочника Модель 

    if type == "techniqueModel":
        item = Technique_model.objects.get(id=id)
    else:
        if type == "engineModel":
            item = Engine_model.objects.get(id=id)
        else:
            if type == "transmissionModel":
                item = Transmission_model.objects.get(id=id)
            else:
                if type == "driveAxleModel":
                    item = Drive_axle_model.objects.get(id=id)
                else:
                    if type == "steerableAxleModel":
                        item = Steerable_axle_model.objects.get(id=id)
                    else:
                        if type == "ServiceCompany":
                            item = Service_company.objects.get(id=id)
    return render(request, 'dictionary.html', {'item': item})

def maintenancedirectory (request, id, type):

    if type == "typeMaintenance":
        item = Type_maintenance.objects.get(id=id)
    else:
        if type == "serviceCompany":
            item = Service_company.objects.get(id=id)
    return render(request, 'dictionary.html', {'item': item})

def сomplaintdirectory (request, id, type):

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
       # Получаем обычный запрос
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            self.filterset = CarFilter(self.request.GET, queryset)
        else:
            self.filterset = CarFilterNoAut(self.request.GET, queryset)          
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context
    
def dictionaries (request):
    return render(request, 'dictionaries.html')
    
class MaintenanceList(LoginRequiredMixin, ListView): #Общий список ТО
    model = Maintenance
    ordering = 'date_work_order'
    template_name = 'Maintenance/Maintenances.html'
    context_object_name = 'maintenances'
    paginate_by = 10


    # def get_queryset(self):
    #    # Получаем обычный запрос
    #     queryset = super().get_queryset()
    #     if self.request.user.is_authenticated:
    #         self.filterset = CarFilter(self.request.GET, queryset)
    #     else:
    #         self.filterset = CarFilterNoAut(self.request.GET, queryset)

class MaintenanceCreate(LoginRequiredMixin, CreateView):
    model = Maintenance
    form_class = CreateMaintenanceForm
    template_name = 'Maintenance/CreateMaintenance.html'
    permission_required = ('silant.create_maintenance',)
    success_url = '/cars/maintenances/'

    def form_valid(self, form): #редирект на список
         self.object = form.save(commit=False)
         self.object.user = self.request.user
         self.object.save()
         return redirect(self.get_success_url())
    

class MaintenanceEdit(LoginRequiredMixin, UpdateView):
    form_class = CreateMaintenanceForm
    model = Maintenance
    template_name = 'Maintenance/CreateMaintenance.html'
    permission_required = ('silant.edit_maintenance', )
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
    context_object_name = 'сomplaints'
    paginate_by = 10


    # def get_queryset(self):
    #    # Получаем обычный запрос
    #     queryset = super().get_queryset()
    #     if self.request.user.is_authenticated:
    #         self.filterset = CarFilter(self.request.GET, queryset)
    #     else:
    #         self.filterset = CarFilterNoAut(self.request.GET, queryset)

class ComplaintsCreate(LoginRequiredMixin, CreateView):
    model = Complaints
    form_class = CreateComplaintsForm
    template_name = 'Complaints/CreateComplaints.html'
    permission_required = ('silant.create_сomplaints',)
    success_url = '/cars/сomplaints/'

    
    def form_valid(self, form): #редирект на список
         self.object = form.save(commit=False)
         self.object.user = self.request.user
         self.object.save()
         return redirect(self.get_success_url())
    

class ComplaintsEdit(LoginRequiredMixin, UpdateView):
    form_class = CreateComplaintsForm
    model = Complaints
    template_name = 'Complaints/CreateComplaints.html'
    permission_required = ('silant.edit_сomplaints', )
    success_url = '/cars/сomplaints/'

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())      