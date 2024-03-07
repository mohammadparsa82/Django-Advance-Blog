from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1" 

router = DefaultRouter()
router.register("post", views.PostModelViewsSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls

""""
urlpatterns = [
    # path('post/', views.PostList, name="post-list"),
    # path('post/<id>/',views.PostDetail,name='post-detail'),
    # path('post/',views.PostList.as_view(),name="post-list"),
    # path('post/<id>/',views.PostDetail.as_view(),name='post-detail'),
    path('post/', views.PostModelViewsSet.as_view({'get':'list','post':'create'}),name='post-list'),
    path('post/<int:pk>', views.PostModelViewsSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='post-detail'),
    path('category/',views.CategoryModelViewSet.as_view({'get':'list','post':'create'}),name='category-list')
]

urlpatterns += router.urls
"""