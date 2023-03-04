from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from .forms import CreateCarForm

from .models import Car, Engine_model, Technique_model


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

def createdirectory (request, id, type): #Функция по форме сохранения каждого справочника Модель 

    if type == "techniqueModel":
        item = Technique_model.objects.get(id=id)
        return render(request, 'dictionary.html', {'item': item})
    else:
        if type == "engineModel":
            item = Engine_model.objects.get(id=id)
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