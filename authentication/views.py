from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


from .models import Profile, Role, Identification_type
from .forms import UserForm, ProfileForm
from . import views
# Create your views here.

class ListUserView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'authentication/list_users.html'
    context_object_name = 'profiles'
    paginate_by = 10
    
    login_url = reverse_lazy('authentication:login')
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for profile in context['profiles']:
            profile.user_status = 'active' if profile.user.is_active else 'deactivate'
        return context
    

class RegisterUserView (LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    secomd_form_class = UserForm
    template_name = 'authentication/register_user.html'
    success_url = '/'

    login_url = reverse_lazy('authentication:login')
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
        print(form['id_type'].field.choices)  # Verifica las opciones de 'id_type'
        print(form['role'].field.choices) 
        for field in form.errors:
            print(f"Error en el campo '{field}': {form.errors[field]}")

        print(form.errors)
        messages.error(
            self.request, 'Error al crear el usuario, por favor verifique los datos ingresados')
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['identification_types'] = Identification_type.objects.values_list('type', flat=True)
        context['roles'] = Role.objects.values_list('rol_name', flat=True)
        return context


class LoginUserView(LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('dashboard:index')

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'message':'error al iniciar sesion'})

    def form_valid(self, form):
        response = super().form_valid(form)
        return JsonResponse({'success': True, 'url': self.success_url})



class LogoutUserView(LogoutView):
    next_page = reverse_lazy('authentication:login')

