from rest_framework import generics

from apps.user.models import User
from apps.user.serializers import UserCreateSerializer
from apps.user.permissions import IsOwner


class UserListCreateApiView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserCreateSerializer


class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserCreateSerializer 
    permission_classes=[IsOwner]