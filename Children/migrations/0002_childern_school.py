# Generated by Django 3.0.8 on 2020-07-26 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
        ('Children', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='childern',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='studentSchool', to='School.School', verbose_name='School'),
        ),
    ]
