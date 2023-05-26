from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
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
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .models import Profile, Role, Identification_type
from .forms import UserForm, ProfileForm
from . import views
# Create your views here.

class ListUserView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'authentication/list_users.html'
    context_object_name = 'profiles'

    
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
    success_url = reverse_lazy('authentication:list_user')

    login_url = reverse_lazy('authentication:login')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        user_form = self.secomd_form_class(self.request.POST)
        print(user_form)
        if user_form.is_valid():
            user = user_form.save()
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            response = super().form_valid(form)
            messages.success(
                self.request, 'Usuario creado correctamente')
            return JsonResponse(data={'success': True, 'url': self.success_url})
        else:
            return self.form_invalid(form)


    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el usuario, por favor verifique los datos ingresados')
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'message': 'Error al crear el usuario', 'errors': errors})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['identification_types'] = Identification_type.objects.values_list('type', flat=True)
        context['roles'] = Role.objects.values_list('rol_name', flat=True)
        return context

class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    second_form_class = UserForm
    template_name = 'authentication/update_user.html'
    success_url = reverse_lazy('authentication:list_user')
    success_message = "Usuario actualizado correctamente"

    login_url = reverse_lazy('authentication:login')
    redirect_field_name = 'redirect_to'

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('user_id')  # Obtener el ID del usuario de la URL
        user = get_object_or_404(get_user_model(), id=user_id)  # Obtener la instancia del usuario o mostrar 404 si no existe
        return user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['identification_types'] = Identification_type.objects.values_list('type', flat=True)
        context['roles'] = Role.objects.values_list('rol_name', flat=True)
        return context

    def form_valid(self, form):
        user_id = self.kwargs.get('user_id')  # Obtener el ID del usuario de la URL
        user = get_object_or_404(get_user_model(), id=user_id)  # Obtener la instancia del usuario o mostrar 404 si no existe
        user_form = self.second_form_class(self.request.POST, instance=user)
        if user_form.is_valid():
            user = user_form.save()
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(self.request, self.success_message)
            return JsonResponse(data={'success': True, 'url': self.success_url})
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar el usuario, por favor verifique los datos ingresados')
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'message': 'Error al actualizar el usuario', 'errors': errors})

class DeactivateUserView(View):
    template_name = 'authentication/deactivate_user.html'
    success_url = reverse_lazy('authentication:list_user')

    def post(self, request, *args, **kwargs):
        print(kwargs)
        profile = kwargs.get('profile_id')
        profile = get_object_or_404(Profile, id=profile)
        user = profile.user
        user.is_active = False
        user.save()
        messages.success(self.request, 'Usuario desactivado correctamente')
        return redirect(self.success_url)

    def get(self, request, *args, **kwargs):
        profile = kwargs.get('profile_id')
        profile = get_object_or_404(Profile, id=profile)
        user = profile.user
        context = {
            'user': user
        }
        return render(request, self.template_name, context)

class ActivateUserView(View):
    template_name = 'authentication/activate_user.html'
    success_url = reverse_lazy('authentication:list_user')

    def post(self, request, *args, **kwargs):
        print(kwargs)
        profile = kwargs.get('profile_id')
        profile = get_object_or_404(Profile, id=profile)
        user = profile.user
        user.is_active = True
        user.save()
        messages.success(self.request, 'Usuario activado correctamente')
        return redirect(self.success_url)

    def get(self, request, *args, **kwargs):
        profile = kwargs.get('profile_id')
        profile = get_object_or_404(Profile, id=profile)
        user = profile.user
        context = {
            'user': user
        }
        return render(request, self.template_name, context)



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

