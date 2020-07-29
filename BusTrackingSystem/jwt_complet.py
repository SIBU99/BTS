from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
#!serialization section
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        if user.parentAuth.all():
            del token["user_id"]
            parent = user.parentAuth.all()[0]
            token["acc_type"] = "Parent"
            token["name"] = parent.fullname
            token["id"] = parent.id
            token["child"] = parent.childrens_id if parent.childrens_id else None
            token["child_name"] = parent.childrens_name if parent.childrens_name else None
        elif user.employeeAuth.all():
            del token["user_id"]
            employee = user.employeeAuth.all()[0]
            token["acc_type"] = employee.job
            token["name"] = employee.fullname
            token["id"] = employee.id
            token["school_name"] = employee.school.name
            token["school_id"] = employee.school.id
        return token

#! View Section
class ObtainTokenPairWithDataView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

#!url Section
urlpatterns = [
    path('token/obtain/', ObtainTokenPairWithDataView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]