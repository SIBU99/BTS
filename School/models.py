from django.db import models
from Children.validators import (
    phoneVerify,
)
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class School(models.Model):
    "this will hold the information of the School"
    name = models.CharField(
        verbose_name="Name",
        help_text="School's Name",
        max_length=120
    )
    phone = models.CharField(
        verbose_name="Phone", 
        help_text="School's phone number", 
        max_length=10,
        validators=[
            phoneVerify
            ]
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

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("School-detail", kwargs={"pk": self.pk})

class School_admin(models.Model):
    "this will hold the information of the School"
    auth = models.ForeignKey(
        User, 
        verbose_name="Admin's Auth", 
        on_delete=models.CASCADE,
        related_name="schoolAdminAuth"
    )
    first_name = models.CharField(
        verbose_name="Firt Name",
        help_text="Admin's First Name",
        max_length=120
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        help_text="Admin's Last Name",
        max_length=120
    )
    phone = models.CharField(
        verbose_name="Phone", 
        help_text="School's phone number", 
        max_length=10,
        validators=[
            phoneVerify
            ]
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
    job = models.CharField(
        verbose_name="Job Profile",
        max_length=120
    )
    school = models.ForeignKey(
        "School.School", 
        verbose_name="School", 
        on_delete=models.CASCADE,
        related_name="adminSchool"
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
        verbose_name = "School Admin"
        verbose_name_plural = "School Admins"

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("SchoolAdmin-detail", kwargs={"pk": self.pk})
