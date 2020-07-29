from django.db import models
from .validators import (
    phoneVerify,
)
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
def uploadProfilePictureChild(instance, filename):
    "this will upload the profile picture of Customer"
    return f"dp/{instance.parent__id}/child/{instance.id}/{filename}"

class Parent(models.Model):
    "this will hold the information of parent"
    auth = models.ForeignKey(
        User, 
        verbose_name="Parent's Auth", 
        on_delete=models.CASCADE,
        related_name="parentAuth"
    )
    first_name = models.CharField(
        verbose_name="Firt Name",
        help_text="Parent's First Name",
        max_length=120
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        help_text="Parent's Last Name",
        max_length=120
    )
    phone = models.CharField(
        verbose_name="Phone1", 
        help_text="Parent's phone number(First)", 
        max_length=10,
        validators=[
            phoneVerify
            ],
    unique=True,
    )
    phone = models.CharField(
        verbose_name="Phone2", 
        help_text="Parent's phone number(Second)", 
        max_length=10,
        validators=[
            phoneVerify
            ]
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="Parent's Email", 
        max_length=254,
        unique=True
    ) 
    address = models.TextField(
        verbose_name="Address",
        help_text = "Parent's Complete Address"
    )
    relation = models.CharField(
        verbose_name="Relation",
        help_text="Relation Name",
        max_length=100
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
    
    @property
    def childrens(self):
        "this will return the list of his/her Children"
        return self.childParent.all()
    
    @property
    def childrens_id(self):
        "this will return the list of his/her Children"
        return self.childParent.all().values_list("id", flat=True)
    
    @property
    def childrens_name(self):
        "this will return the list of his/her Children"
        data = []
        for i in self.childParent.all():
            data.append(i.fullname)
        return data

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("Parent-detail", kwargs={"pk": self.pk})

class Childern(models.Model):
    "this will hold the information of a children"
    parent = models.ForeignKey(
        "Children.Parent", 
        verbose_name="Parent", 
        on_delete=models.CASCADE, 
        related_name="childParent"
    )
    first_name = models.CharField(
        verbose_name="Firt Name",
        help_text="child's First Name",
        max_length=120
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        help_text="Child's Last Name",
        max_length=120
    )
    dp = models.ImageField(
        verbose_name="Profile Picture", 
        upload_to=uploadProfilePictureChild, 
        height_field=None, 
        width_field=None, 
        max_length=None
    )

    school = models.ForeignKey(
        "School.School", 
        verbose_name="School", 
        on_delete=models.SET_NULL, 
        null=True,
        related_name="studentSchool"
    )
    standard = models.CharField(
        verbose_name="Standard(Class)",
        help_text="Child's Class or Stanadard in which it studies",
        max_length=3
    )
    section = models.CharField(
        verbose_name="Section",
        help_text="Child's Section",
        max_length=3
    )
    gender = models.CharField(
        verbose_name="Gender",
        choices =  [
            ("M","Male",),
            ("F","Female",),
            ( "O","Others",),
        ],
        max_length=2,
    )


    pickup_lat = models.CharField(
        verbose_name="Pickup Location(Latitude)",
        max_length=120,
        null=True,
    )
    pickup_long = models.CharField(
        verbose_name="Pickup Location(Longitude)",
        max_length=120,
        null=True,
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

@property
def address(self):
    "this will hold the proper living address of the childern"
    dict_data = dict()
    dict_data["address"] = self.parent.address
    dict_data["city"] = self.parent.city
    dict_data["state"] = self.parent.state
    dict_data["country"] = self.parent.country
    return dict_data

    class Meta:
        verbose_name = "Childern"
        verbose_name_plural = "Childerns"

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("Childern-detail", kwargs={"pk": self.pk})
