from rest_framework.response import Response
from rest_framework import generics,permissions,filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.todo.models import Todo
from apps.todo.serializers import TodoSerializers
from apps.todo.permissions import IsOwner
from apps.todo.filters import TodoFilter

class TodoCreateApiView(generics.CreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



class TodoListApiView(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers
    permission_classes=[IsOwner]
    filterset_class=TodoFilter
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)


class TodoDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers
    permission_classes=[IsOwner]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



class RemoveAllTodoApiView(generics.DestroyAPIView):
    serializer_class=TodoSerializers
    permission_classes=[IsOwner]

    def delete(self, request, *args, **kwargs):
        todo =Todo.objects.filter(user=request.user)
        for i in todo:
            i.delete()
        return Response({'ALL':'DELETED'})

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
