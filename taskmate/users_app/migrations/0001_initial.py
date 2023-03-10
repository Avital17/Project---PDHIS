# Generated by Django 4.1.4 on 2023-01-06 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(choices=[('1', 'doctor'), ('1', 'doctor')], default='doctor', max_length=1)),
                ('department', models.CharField(choices=[('1', 'Otorhinolaryngology'), ('2', 'Cardiology'), ('3', 'Oncology'), ('4', 'Dermatologist'), ('5', 'Endocrinologist'), ('6', 'Gastroenterologist'), ('7', 'Hematologist'), ('8', 'Nephrologists'), ('9', 'Neurologists'), ('10', 'Ophthalmologist')], max_length=50)),
                ('user_doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
