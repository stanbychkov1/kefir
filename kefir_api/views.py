from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import UserSerializer, UserForAdminSerializer
from .permissions import IsAdminOrAuthorOrReadOnly

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrAuthorOrReadOnly,]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return UserForAdminSerializer
        return UserSerializer
