# Generated by Django 3.0.8 on 2020-07-26 08:08

import Children.models
import Children.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Parent's First Name", max_length=120, verbose_name='Firt Name')),
                ('last_name', models.CharField(help_text="Parent's Last Name", max_length=120, verbose_name='Last Name')),
                ('phone', models.CharField(help_text="Parent's phone number(Second)", max_length=10, validators=[Children.validators.phoneVerify], verbose_name='Phone2')),
                ('email', models.EmailField(help_text="Parent's Email", max_length=254, unique=True, verbose_name='Email')),
                ('address', models.TextField(help_text="Parent's Complete Address", verbose_name='Address')),
                ('relation', models.CharField(help_text='Relation Name', max_length=100, verbose_name='Relation')),
                ('country', models.CharField(max_length=120, verbose_name='County')),
                ('state', models.CharField(max_length=120, verbose_name='State')),
                ('city', models.CharField(max_length=120, verbose_name='City')),
                ('verified', models.BooleanField(default=False, verbose_name='Account Verifed')),
            ],
            options={
                'verbose_name': 'Parent',
                'verbose_name_plural': 'Parents',
            },
        ),
        migrations.CreateModel(
            name='Childern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="child's First Name", max_length=120, verbose_name='Firt Name')),
                ('last_name', models.CharField(help_text="Child's Last Name", max_length=120, verbose_name='Last Name')),
                ('dp', models.ImageField(upload_to=Children.models.uploadProfilePictureChild, verbose_name='Profile Picture')),
                ('standard', models.CharField(help_text="Child's Class or Stanadard in which it studies", max_length=3, verbose_name='Standard(Class)')),
                ('section', models.CharField(help_text="Child's Section", max_length=3, verbose_name='Section')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=2, verbose_name='Gender')),
                ('pickup_lat', models.CharField(max_length=120, null=True, verbose_name='Pickup Location(Latitude)')),
                ('pickup_long', models.CharField(max_length=120, null=True, verbose_name='Pickup Location(Longitude)')),
                ('verified', models.BooleanField(default=False, verbose_name='Account Verifed')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childParent', to='Children.Parent', verbose_name='Parent')),
            ],
        ),
    ]
