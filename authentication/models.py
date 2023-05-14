from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


from datetime import datetime
# Create your models here.

class Role(models.Model):
    rol_name = models.CharField(max_length=50)

    def __str__(self):
        return self.rol_name

class Identification_type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=('user'), help_text=('choose user'),
                                related_name='profile', blank=True, null=True)

    phone_number = models.CharField(max_length=20, blank=False,
                                    verbose_name=('phone number'), help_text=('phone number'))
    address = models.CharField(max_length=100, blank=True,
                               verbose_name=('address'), help_text=('address'))

    image = models.ImageField(upload_to='profile_images', blank=True,
                              verbose_name=('image'), help_text=('image'))

    info_extra = models.TextField(blank=True,
                                  verbose_name=('info extra'), help_text=('info extra'))

    id_type = models.ForeignKey(Identification_type, on_delete=models.CASCADE, related_name='id_type')

    identification = models.CharField(max_length=20, blank=True,
                                        verbose_name=('identification'), help_text=('identification'))
                        
    birthday = models.DateField(blank=True, null=True,
                                 verbose_name=('bithday'), help_text=('bithday'))

    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

