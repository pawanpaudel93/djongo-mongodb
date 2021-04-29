from rest_framework.routers import DefaultRouter
from django.urls import path, include


from blogs.views import PostViewSet

router = DefaultRouter()
router.register('', PostViewSet, basename='post')
 
urlpatterns = [ 
    path('', include(router.urls)),
]