from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from usersapp.models import MyCustomUser
from usersapp.serializers import MyCustomUserSerializers


class MyCustomUserModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = MyCustomUser.objects.all()
    serializer_class = MyCustomUserSerializers
