from django.urls import path , include
from .views import * 
app_name = "api-v1" 

urlpatterns = [
    #registration
    path('registration/', RegistrationApiView.as_view(),name='registration'),

]