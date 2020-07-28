from django.contrib import admin
from .models import (
    Childern,
    Parent
)
# Register your models here.
admin.site.register(Childern)
admin.site.register(Parent)