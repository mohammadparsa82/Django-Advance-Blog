from django.urls import path , include
from .views import * 

app_name = "api-v1" 

urlpatterns = [
    #path('post/', PostList, name="post-list"),
    #path('post/<id>/',PostDetail,name='post-detail'),
    path('post/',PostList.as_view(),name="post-list"),
    path('post/<id>/',PostDetail.as_view(),name='post-detail'),
]