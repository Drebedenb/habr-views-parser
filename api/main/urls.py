from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewsDataViewSet

router = DefaultRouter()
router.register(r'', ViewsDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
