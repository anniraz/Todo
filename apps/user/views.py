from rest_framework import generics

from apps.user.models import User
from apps.user.serializers import UserCreateSerializer


class UserListCreateApiView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserCreateSerializer

    