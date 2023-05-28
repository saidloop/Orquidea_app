from django.shortcuts import render
from django.views.generic import ListView
from .models import Contract

# Create your views here.
class ListContracts(ListView):
    model = Contract
    template_name = 'contracts/list_contracts.html'
    context_object_name = 'contracts'
    paginate_by = 10

class CreateContractView(CreateView):
    model = Contract
    template_name = 'contracts/create_contract.html'
    form_class = ContractForm
    success_url = reverse_lazy('contracts:list_contracts')