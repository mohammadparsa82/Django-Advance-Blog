from django.urls import path , include
from .views import * 
#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "api-v1" 

urlpatterns = [

    #registration
    path('registration/', RegistrationApiView.as_view(),name='registration'),

    # login token
    path('token/login/', CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiscardAuthToken.as_view(), name='token-logout'),

    # jwt login
    path('jwt/login/' ,TokenObtainPairView.as_view(), name='jwt-login'),
    path('jwt/refresh/' , TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/' , TokenVerifyView.as_view(), name='jwt-verify'),
]