from django import forms
from .models import Contract, Client, Beneficiary

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('firts_name', 'last_name', 'birthday', 'identification', 'expedition_place', 'email', 'address', 'phone_number', 'transfer')


class BeneficiaryForm(forms.ModelForm):
    
        class Meta:
            model = Beneficiary
            fields = ('firts_name', 'last_name', 'birthday', 'identification', 'kinship')




class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('contract_number', 'expedition_date', 'client', 'plan', 'Asesor', 'Beneficiary')

    client = ClientForm()
    Beneficiary  = BeneficiaryForm()
    

    def save(self, commit=True):
        contract = super().save(commit=False)
        client_form = ClientForm(self.cleamed_data['client'])
        if client_form.is_valid():
            client = client_form.save()
            contract.client = client
            
        beneficiary_form = BeneficiaryForm(self.cleaned_data['beneficiary'])
        if beneficiary_form.is_valid():
            beneficiary = beneficiary_form.save()
            contract.beneficiary = beneficiary

        if commit:
            contract.save()


                
        return contract