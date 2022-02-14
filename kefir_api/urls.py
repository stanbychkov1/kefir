from django.urls import path, include

from .routers import CustomReadOnlyRouter
from .views import UserViewSet


router = CustomReadOnlyRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
