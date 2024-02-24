from django.urls import path
from .views import * 
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
app_name = "blog" 

urlpatterns = [
    #path('cbv-index', IndexView.as_view(),name='cbv-index'),
    #path('go-to-django/<int:pk>', RedirectToDjango.as_view(),name='redirect-to-django'),
    path('post/',Postlist.as_view(),name='post-list'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/create/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/edit/',PostEditView.as_view(),name='post-edit')


]