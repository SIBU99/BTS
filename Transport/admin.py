from django.contrib import admin
from .models import(
    Employee,
    Vehicle,
    BusRoute,
    TravelLog,
    TravelHistory,
)
# Register your models here.
admin.site.register(Employee)
admin.site.register(Vehicle)
admin.site.register(BusRoute)
admin.site.register(TravelLog)
admin.site.register(TravelHistory)