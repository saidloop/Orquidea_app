# Generated by Django 4.0.6 on 2023-05-09 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_bithday_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_type', to='authentication.identification_type'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='authentication.role'),
        ),
    ]