from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ContractForm

from .models import Contract, Plan, Profile, kinship

# Create your views here.
class ListContracts(ListView):
    model = Contract
    template_name = 'contracts/list_contracts.html'
    context_object_name = 'contracts'
    
    
class RegisterContractView(LoginRequiredMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'register_contract.html'
    success_url = '/contracts/list_contracts'
    
    login_url = '/authentication/login'
    redirect_field_name = 'redirect_to'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        messages.success(
            self.request, 'Contrato creado correctamente')
        return JsonResponse(data={'sucess' : True, 'url' : self.success_url})

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el contrato')
        return JsonResponse(data={'sucess' : False, 'errors' : form.errors})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plans'] = Plan.objects.values_list('name', flat=True)
        context['asesores'] = Profile.objects.values_list('user__username', flat=True)
        context['kinships'] = kinship.objects.values_list('name', flat=True)
        print(context['kinships'])
        return context
