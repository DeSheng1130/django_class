from rest_framework import viewsets

from todo.models import Todo

from .serializers import TodoSerializers


class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
