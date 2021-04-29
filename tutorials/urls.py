from rest_framework.routers import DefaultRouter
from django.urls import path, include


from tutorials.views import TutorialViewSet

router = DefaultRouter()
router.register('', TutorialViewSet, basename='tutorial')
 
urlpatterns = [ 
    path('', include(router.urls)),
]