from django.db import models
from Children.validators import (
    phoneVerify,
)
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
def uploadLogFile(instance, filename):
    "this will upload the profile picture of Customer"
    date = timezone.now()
    data = date.strftime("%a, %d-%b,%Y")
    return f"log/{instance.school.name}/{instance.vehicle.no}/{data}/{filename}"
class Employee(models.Model):
    "this will hold the information of the School"
    auth = models.ForeignKey(
        User, 
        verbose_name="Employee's Auth", 
        on_delete=models.CASCADE,
        related_name="employeeAuth"
    )
    first_name = models.CharField(
        verbose_name="Firt Name",
        help_text="Employee's First Name",
        max_length=120
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        help_text="Employee's Last Name",
        max_length=120
    )
    phone = models.CharField(
        verbose_name="Phone", 
        help_text="Employee's phone number", 
        max_length=10,
        validators=[
            phoneVerify
            ]
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="Employee's Email", 
        max_length=254,
        unique=True
    ) 
    address = models.TextField(
        verbose_name="Address",
        help_text = "Employee's Complete Address"
    )
    country = models.CharField(
        verbose_name="County",
        max_length=120
    )
    state = models.CharField(
        verbose_name="State",
        max_length=120
    )
    city = models.CharField(
        verbose_name="City",
        max_length=120
    )
    job = models.CharField(
        verbose_name="Job Profile",
        max_length=120
    )
    vehicle = models.ForeignKey(
        "Transport.Vehicle", 
        verbose_name="Employee's Vehicle", 
        on_delete=models.CASCADE,
        related_name="employeeVehicle"
    )
    school = models.ForeignKey(
        "School.School", 
        verbose_name="School", 
        on_delete=models.CASCADE,
        related_name="employeeSchool"
    )
    verified = models.BooleanField(
        verbose_name = "Account Verifed", 
        default = False
    )

    @property
    def fullname(self):
        "returns the fullname of Child"
        first_name = self.first_name.split(" ")
        name = [i.capitalize() for i in first_name] + [self.last_name.capitalize()]
        return " ".join(name)
    

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={"pk": self.pk})

class Vehicle(models.Model):
    "this will hold the information of the School"
    no = models.CharField(
        verbose_name="Vehicle No",
        primary_key = True,
        null = False,
        max_length=50,
        unique = True
    )
    no_of_seat = models.IntegerField(
        verbose_name="Seats", 
        help_text="No of students travel in That Bus",
        default = 0,
    )
    route_no = models.ForeignKey(
        "Transport.BusRoute", 
        verbose_name="Route No",
        help_text = "Bus Route Nuber", 
        on_delete=models.CASCADE,
        related_name="vehicleBusRoute"
    )
    country = models.CharField(
        verbose_name="County",
        max_length=120
    )
    state = models.CharField(
        verbose_name="State",
        max_length=120
    )
    city = models.CharField(
        verbose_name="City",
        max_length=120
    )

    @property
    def employees(self):
        "this will return the Employees Detail"
        return self.employeeVehicle.all()

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        return self.no

    def get_absolute_url(self):
        return reverse("vehicle-detail", kwargs={"pk": self.pk})

class BusRoute(models.Model):
    "this will hold the information of the School"
    #!Endpoint 1
    endpoint1 = models.CharField(
        verbose_name="Endpoint1",
        help_text="One end of route",
        max_length=120
    )
    endpoint1_lat = models.CharField(
        verbose_name="Endpoint1 Location(Latitude)",
        max_length=120,
        null=True,
    )
    endpoint1_long = models.CharField(
        verbose_name="Endpoint1 Location(Longitude)",
        max_length=120,
        null=True,
    )
    #!Endpoint 2
    endpoint2 = models.CharField(
        verbose_name="Endpoint2",
        help_text="Another end of route",
        max_length=120
    )
    endpoint2_lat = models.CharField(
        verbose_name="Endpoint2 Location(Latitude)",
        max_length=120,
        null=True,
    )
    endpoint2_long = models.CharField(
        verbose_name="Endpoint2 Location(Longitude)",
        max_length=120,
        null=True,
    )

    via = models.TextField(
        verbose_name="Via Area",
        help_text = "This contain the comma separetes values like ' test1,test2,test3, ..'",
        default = "",
        blank=True
    )

    country = models.CharField(
        verbose_name="County",
        max_length=120
    )
    state = models.CharField(
        verbose_name="State",
        max_length=120
    )
    city = models.CharField(
        verbose_name="City",
        max_length=120
    )

    class Meta:
        verbose_name = "Bus Route"
        verbose_name_plural = "Bus Routes"
    
    @property
    def vehicles_under(self):
        "this will return the vehicle under this route"
        return self.vehicleBusRoute.all()

    @property
    def via_area(self):
        return self.via.split(",")

    def __str__(self):
        return f"{self.id} | {self.endpoint1} | {self.endpoint2} "
        

    def get_absolute_url(self):
        return reverse("busRoute-detail", kwargs={"pk": self.pk})

class TravelLog(models.Model):
    "this will hold the information of the School"
    children = models.ForeignKey(
        "Children.Childern", 
        verbose_name="Children",
        help_text = "Children Account Linked", 
        on_delete=models.SET_NULL,
        null=True,
        related_name="childrenTravelLog"
    )
    travel_history = models.ForeignKey(
        "Transport.TravelHistory", 
        verbose_name="Travel History",
        help_text = "Travel History", 
        on_delete=models.SET_NULL,
        null=True,
        related_name="travelHistoryTravelLog"
    ) 
    pickup_lat = models.CharField(
        verbose_name="Pickup Latitude",
        max_length=120
    )
    pickup_long = models.CharField(
        verbose_name="Pickup Longitude",
        max_length=120
    )
    pickup_date_time = models.DateTimeField(
        verbose_name="Pickup Date Time",
        auto_now_add = True,  
    )
    pickup_notified = models.BooleanField(
        verbose_name = "Pickup Notified",
        help_text = "To concern Parent of child" ,
        default = False
    )

    drop_lat = models.CharField(
        verbose_name="Drop Latitude",
        max_length=120
    )
    drop_long = models.CharField(
        verbose_name="Drop Longitude",
        max_length=120
    )
    drop_date_time = models.DateTimeField(
        verbose_name="Drop Date Time",
        null = True,
        blank = True,  
    )
    drop_notification = models.BooleanField(
        verbose_name = "Drop Notified",
        help_text = "To concern Parent of child" ,
        default = False
    )

    parent_phone = models.CharField(
        verbose_name="Parent Phone", 
        help_text="Parent's phone number of concern Child", 
        max_length=10,
        validators=[
            phoneVerify
            ]
    )
    parent_email = models.EmailField(
        verbose_name="Email",
        help_text="Employee's Email", 
        max_length=254,
        unique=True
    ) 

    class Meta:
        verbose_name = "Travel Log"
        verbose_name_plural = "Travel Logs"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("travelLog-detail", kwargs={"pk": self.pk})

class TravelHistory(models.Model):
    "this will hold the information of the Travel History"
    school = models.ForeignKey(
        "School.School", 
        verbose_name="School", 
        on_delete=models.CASCADE,
        related_name="travelHistorySchool"
    )
    vehicle = models.ForeignKey(
        "Transport.Vehicle", 
        verbose_name="Vehicle", 
        on_delete=models.CASCADE,
        related_name="travelHistoryVehicle"
    )
    log_file = models.FileField(
        verbose_name="Log File", 
        upload_to=uploadLogFile, 
        null =True,
        blank = True,
    )
    children = models.ManyToManyField(
        "Children.Childern", 
        verbose_name="Childrens",
        through="TravelLog",
        related_name="travelHistory",
    )


    class Meta:
        verbose_name = "Travel History"
        verbose_name_plural = "Travel Historys"

    def __str__(self):
        return f"{self.school.name} | {self.vehicle.no}"

    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={"pk": self.pk})