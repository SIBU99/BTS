from django.contrib import admin
from .models import (
    School,
    School_admin,
)
# Register your models here.
admin.site.register(School)
admin.site.register(School_admin)