from django.db import models
from authentication.models import Profile

# Create your models here.

class Client (models.Model):
    firts_name = models.CharField(max_length=100, blank=False, verbose_name=('nombres'), help_text=('nombres'))
    last_name = models.CharField(max_length=100, blank=False, verbose_name=('apellidos'), help_text=('apellidos'))
    birthday = models.DateField(blank=True, null=True,
                                 verbose_name=('fecha de nacimiento'), help_text=('fecha de nacimiento'))
    identification = models.CharField(max_length=100, blank=False, verbose_name=('numero de identificacion'), help_text=('numero de identificacion'))
    expedition_place = models.CharField(max_length=100, blank=False, verbose_name=('lugar de expedicion'), help_text=('lugar de expedicion'))
    email = models.CharField(max_length=100, blank=False, verbose_name=('correo electronico'), help_text=('correo electronico'))
    address = models.CharField(max_length=100, blank=False, verbose_name=('direccion'), help_text=('direccion'))
    phone_number = models.CharField(max_length=100, blank=False, verbose_name=('numero de telefono'), help_text=('numero de telefono'))
    transfer = models.CharField(max_length=100, blank=True, verbose_name=('transferencia'), help_text=('transferencia'))


    def __str__(self):
        return self.name

class Plan (models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name=('nombre'), help_text=('nombre'))
    description = models.CharField(max_length=100, blank=False, verbose_name=('descripcion'), help_text=('descripcion'))

    def __str__(self):
        return self.name

class kinship (models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name=('nombre del parentesco'), help_text=('nombre del parentesco'))

    def __str__(self):
        return self.name

class Beneficiary (models.Model):
    firts_name = models.CharField(max_length=100, blank=False, verbose_name=('nombres'), help_text=('nombres'))
    last_name = models.CharField(max_length=100, blank=False, verbose_name=('apellidos'), help_text=('apellidos'))
    birthday = models.DateField(blank=True, null=True,
                                 verbose_name=('fecha de nacimiento'), help_text=('fecha de nacimiento'))
    identification = models.CharField(max_length=100, blank=False, verbose_name=('numero de identificacion'), help_text=('numero de identificacion'))
    kinship = models.ForeignKey(kinship, on_delete=models.CASCADE, verbose_name=('parentesco'), help_text=('parentesco'))

    def __str__(self):
        return self.name

class Contract (models.Model):
    contract_number = models.CharField(max_length=100)
    expedition_date = models.DateField(blank=True, null=True,
                                    verbose_name=('fecha de expedicion'), help_text=('fecha de expedicion'))
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=('cliente'), help_text=('cliente'))
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name=('plan'), help_text=('plan'))
    Asesor = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=('Asesor'), help_text=('Asesor'))
    Beneficiary = models.ManyToManyField(to=Beneficiary, verbose_name=('beneficiario'), help_text=('beneficiario'))


