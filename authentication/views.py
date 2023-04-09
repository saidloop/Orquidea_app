from django.shortcuts import render

from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.models import User
from .models import Profile, Role
from .forms import UserForm, ProfileForm
# Create your views here.


class RegisterUserView (CreateView):
    model = Profile
    form_class = ProfileForm
    secomd_form_class = UserForm
    template_name = 'authentication/create_user.html'
    success_url = '/'

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        user_form = self.secomd_form_class(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            response = super().form_valid(form)
            messages.success(
                self.request, 'Usuario creado correctamente')
            return response


    def form_invalid(self, form):
        print(form.errors)
        messages.error(
            self.request, 'Error al crear el usuario, por favor verifique los datos ingresados')
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roles'] = Role.objects.values_list('rol_name', flat=True)
        return context


class LoginUserView(LoginView):
    template_name = 'authentication/login.html'

    def form_invalid(self, form):
        messages.error(
            self.request, 'Error al iniciar sesión, por favor verifique los datos ingresados')
        response = super().form_invalid(form)
        return response
    

