from django.db import models
from Children.validators import (
    phoneVerify,
)
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
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
        max_length=50,
        unique = True
    )
    no_of_seat = models.IntegerField(
        verbose_name="Seats", 
        help_text="No of students travel in That Bus",
        default = 0,
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="School's Email", 
        max_length=254,
        unique=True
    ) 
    address = models.TextField(
        verbose_name="Address",
        help_text = "School's Complete Address"
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
