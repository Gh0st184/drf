from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from usersapp.models import MyCustomUser
from usersapp.serializers import MyCustomUserSerializers


class MyCustomUserModelViewSet(ModelViewSet):
    queryset = MyCustomUser.objects.all()
    serializer_class = MyCustomUserSerializers
