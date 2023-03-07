from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from .filters import CarFilter,CarFilterNoAut
from .forms import CreateCarForm, CreateMaintenanceForm

from .models import Car, Drive_axle_model, Engine_model, Maintenance, Service_company, Steerable_axle_model, Technique_model, Transmission_model


class CarCreate(CreateView):
    model = Car
    form_class = CreateCarForm
    template_name = 'CreateCar.html'
    permission_required = ('silant.create_car',)

    #def form_valid(self, form):
    #    self.object = form.save(commit=False)
    #    self.object.user = self.request.user
    #    self.object.save()
    #    return HttpResponseRedirect(self.get_success_url())

class CarEdit(UpdateView):
    form_class = CreateCarForm
    model = Car
    template_name = 'CreateCar.html'
    permission_required = ('silant.edit_car', )

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())

def viewdirectory (request, id, type): #Функция по форме сохранения каждого справочника Модель 

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
    
class MaintenanceList(ListView): #Общий список ТО
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

class MaintenanceCreate(CreateView):
    model = Maintenance
    form_class = CreateMaintenanceForm
    template_name = 'Maintenance/CreateMaintenance.html'
    permission_required = ('silant.create_maintenance',)

    def form_valid(self, form):
       self.object = form.save(commit=False)
       self.object.user = self.request.user
       self.object.save()
       return HttpResponseRedirect(self.get_success_url())

class MaintenanceEdit(UpdateView):
    form_class = CreateMaintenanceForm
    model = Maintenance
    template_name = 'Maintenance/CreateMaintenance.html'
    permission_required = ('silant.edit_maintenance', )

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())          